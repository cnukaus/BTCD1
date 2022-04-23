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

str = sha256(sys.argv[1].encode("utf-8")).hexdigest() + "00"
print(str)

bin_pk = bin(int(str, 16))[2:]  # remove leading 0B
bin_chunks = [bin_pk[i * 11 : (i + 1) * 11] for i in range(24)]
bip_f = "BIP39.txt"

with open(bip_f) as f:
    content = f.read()
bip = content.split("\n")
aa = bip[19]
# print(repr(aa))  # saved me from readline() with has extra newline chr

for bin in bin_chunks:
    print(bip[int(bin, 2) - 1], bin, int(bin, 2) - 1)
