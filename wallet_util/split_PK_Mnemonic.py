import sys
from hashlib import sha256

# input_ = input('Enter something: ') print(sha256(input_.encode('utf-8')).hexdigest())


"""
str = (
    "87191fd766c88cf9efa0da5615dd8bd721279dc983a0029b34a6496b18b63a4c" + "00"
)  # sha256 with padding 2 ending 0, to make it 2 ^11 * 24, which is 264 bits = 11 * 24
assert (
    int(str, 16)
    == 15643296127157775744451174835770482900145205569549578426575496116200505031150592
)
with open(bip_f) as f:
    contents = f.read()
bip = contents.split('\n')
aa = bip[19]

for bin in bin_chunks:
    print(bip[int(bin, 2) - 1], bin, int(bin, 2) - 1)"""


str = sys.argv[1] + "00"
str = sha256(sys.argv[1].encode("utf-8")).hexdigest() + "00"
print(str)


print(
    bin(int(str, 16))
    == bin(
        int(
            "100001110001100100011111110101110110011011001000100011001111100111101111101000001101101001010110000101011101110110001011110101110010000100100111100111011100100110000011101000000000001010011011001101001010011001001001011010110001100010110110001110100100110000000000",
            2,
        )
    )
)

bin_pk = bin(int(str, 16))[2:]  # remove leading 0B

print([i for i in range(3)])
bin_chunks = [bin_pk[i * 11 : (i + 1) * 11] for i in range(24)]
print(bin_chunks)


bip_f = "BIP39.txt"


with open(bip_f) as f:
    content = f.read()
bip = content.split("\n")
aa = bip[19]
# print(repr(aa))  # saved me from readline() with has extra newline chr

for bin in bin_chunks:
    print(bip[int(bin, 2) - 1], bin, int(bin, 2) - 1)
