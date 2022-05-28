import sys
from hashlib import sha256
import binascii

import secrets


def to_mnemonic(data):

    """
    data: secrets.token_bytes(strength // 8)
        b'\\xebr\\x17D*t\\xae\\xd4\\xe3S\\xb6\\xe2\\xebP1\\x8b'
    """
    if len(data) not in [16, 20, 24, 28, 32]:  # I added 64
        raise ValueError(
            "Data length should be one of the following: [16, 20, 24, 28, 32], but it is not (%d)."
            % len(data)
        )
    h = sha256(data).hexdigest()
    b = (
        bin(int(binascii.hexlify(data), 16))[2:].zfill(len(data) * 8)
        + bin(int(h, 16))[2:].zfill(256)[: len(data) * 8 // 32]
    )
    result = []
    for i in range(len(b) // 11):
        idx = int(b[i * 11 : (i + 1) * 11], 2)
        result.append(bip[idx])
    """if (
        detect_language(" ".join(result)) == "japanese"
    ):  # Japanese must be joined by ideographic space.
        result_phrase = u"\u3000".join(result)
    else:"""
    result_phrase = " ".join(result)
    return result_phrase


"""
m = mnemonic.Mnemonic('english')
for word in english:
    tested = your23words + ' ' + word
    if m.check(tested):
        print tested

# or https://www.reddit.com/r/crypto/comments/684zvj/need_help_generating_lastword_checksum_for_bip39/dgvq3ca/

# or check terra sdk mnemonic.py




"""

# https://medium.com/bitbees/python-code-to-manually-create-12-24-worded-seed-and-passphrase-without-trusting-bitcoin-wallets-9d158535dfc6
# input_ = input('Enter something: ') print(sha256(input_.encode('utf-8')).hexdigest())

# to get digest tryhttps://github.com/mcdallas/cryptotools/blob/master/cryptotools/transformations.py


# this will random generate 24 words valid mnemonic
print(to_mnemonic(secrets.token_bytes(128 // 4)))
