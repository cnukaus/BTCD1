
# now updated to
#from eth_utils.encoding import big_endian_to_int


#pip install eth-keys
from eth_keys import keys
from eth_utils.hexadecimal import decode_hex


priv_key_bytes = decode_hex('0xdc')  #reuslt is case insensitive

priv_key = keys.PrivateKey(priv_key_bytes)
pub_key = priv_key.public_key
print(pub_key.to_checksum_address())
assert pub_key.to_hex() == '0xcab'
'''
Getting the Address
Just in case the question was intending to ask about the address...

There are simpler ways to generate the address from scratch, but since we've already done the eth-keys setup, this is a one-liner:
'''
assert pub_key.to_checksum_address() == '0xa0784ba3fcea41fD65a7A47b4cc1FA4C3DaA326f'
