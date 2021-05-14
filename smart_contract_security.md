[原文](https://medium.com/@danrobinson/ethereum-is-a-dark-forest-ecc5f0505dff)
一些优秀的以太坊安全工程师帮助我们制定了一个瞒天过海的计划。除了将调用隐藏为内部交易之外，我们还将交易分为两部分：一个激活我们合约的 set 交易，以及一个拯救激活（如果合约已激活）资金的 get 交易。以如下路径实现：

部署一个 Getter 合约，由其主人调用，只有在激活后才会做出 burn 调用，否则恢复原状。
部署一个 Setter 合约，由其主人调用，将激活 Getter 合约。
在同一区块提交 set 交易和 get 交易。
真实存在的以太坊 DeFi「黑暗森林」：mempool 套利机器人吞噬了我的交易我们智能合约的代码

如果攻击者只试图执行这一 get 交易，就会在不调用 burn 功能的情况下让合约恢复原状。我们原本希望的是在攻击者先后执行 set 和 get 交易，发现内部调用 pool.burn 的指令，然后试图对我们超车时，我们已经完成了交易。

我们拯救这笔钱的代码脚本：

#!/usr/bin/env node

const ethers = require('ethers')

const WHITEHAT = [
    "function get()"
]
const SETTER = [
    "function set(address whiteHat, bool on)"
];

(async () => {
    const provider = new ethers.providers.JsonRpcProvider("http://localhost:8545");

    const dest = process.env.DEST
    console.log("Dest balance before:", await provider.getBalance(dest))

    const whitehatAddress = process.env.WHITEHAT

    const gasPrice1 = 160 * 1e9
    // 20% higher
    const gasPrice2 = gasPrice1 * 1.2

    // call Whitehat.set(on) indirectly via the setter contract by the Setter account
    const setterWallet = new ethers.Wallet(process.env.SETTER_KEY)
    const setterClient = setterWallet.connect(provider);
    const setter = new ethers.Contract(process.env.SETTER, SETTER, setterClient)
    const tx1 = await setter.set(whitehatAddress, true, { gasPrice: gasPrice2 })
    console.log("Submitted",  tx1);

    // call whitehat.get by the Getter account
    const getterWallet = new ethers.Wallet(process.env.GETTER_KEY)
    const whitehatClient = getterWallet.connect(provider);
    const whitehat = new ethers.Contract(whitehatAddress, WHITEHAT, whitehatClient)
    const tx2 = await whitehat.get({ gasLimit: 2e6, gasPrice: gasPrice1 })

    console.log(await tx1.wait())
    console.log(await tx2.wait())

    console.log("Dest balance after:", await provider.getBalance(dest))
})()
但出乎我们意料的是，这个 get 交易会被 Infura 拒绝，即使我们手动覆盖 Gas 估算器也是如此。经过多次失败的尝试后和重新设置后，我们越来越感到时间压力，抱着一丝侥幸心理，我们让第二个交易滑进之后的区块。

这成了一个致命的错误。

我们的 get 交易确实被收录进了较早的区块，但一个 UniswapV2: INSUFFICIENT_LIQUIDITY_BURNED 错误，意味着其在 Uniswap 的流动性消失了。结果我们的 get 交易刚刚进入 mempool 几秒钟，就有人执行了调用，卷走了这笔钱。黑暗森林里的怪兽还是吞噬了我们
