const { vote_on } = require('./snapshot')
const { get_account, accounts } = require('./accounts')
//const delay = ms => new Promise(res => setTimeout(res, ms));

const space = 'uniswap'
const list_space=['uniswap']
//'uniswap','opcollective.eth','aave.eth',banklessvault.eth,shapeshiftdao.eth (only 0x5be,) ffdao.eth (only 0x8477 has NFT)，lido-snapshot.eth，reunitdao.eth (stargate.finance)

// https://snapshot.org/#/shellprotocol.eth/proposal/0x4b9d159e8a7970ea8fc940821b6ce0b17c1ab9e9f510ce28637c13cce0377fb6

const choice = 1

async function mass_voting(space, choice) {
  for (const account of accounts) {
    await new Promise(r => setTimeout(r, 2000));
    await vote_on(account, space, choice)
  }
}

async function loop_voting(list_space, choice) {

  for (account of accounts) {
    await new Promise(r => setTimeout(r, Math.floor(Math.random() * 20) + 1)*1000);
    for (space_ of list_space)
	{	
    		await vote_on(account, space_, choice)
        

	}
  }
}

async function single_voting(account, space, choice) {
  await vote_on(account, space, choice)
}

//mass_voting(space, choice).then()
loop_voting(list_space, choice).then()
//single_voting(get_account(3), space, choice).then()