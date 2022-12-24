from hashlib import sha256
from eth_keys import keys
from eth_utils.hexadecimal import decode_hex

def pk_to_addr(pk):
  '''pk can be '0xhex' or 'hex..'''
  
    priv_key_bytes = decode_hex(pk)  #reuslt is case insensitive, working. Whether has prefix 0x also doesn't change output

    priv_key = keys.PrivateKey(priv_key_bytes)
    pub_key = priv_key.public_key
    return pub_key.to_checksum_address()
    #assert pub_key.to_hex() == '0xcab'
    #assert pub_key.to_checksum_address() == '0xa0784ba3fcea41fD65a7A47b4cc1FA4C3DaA326f'
    
input_ = input('Enter something: ') 

def rep_hash(times,inp):
    i=0
    for n in range(times):
        if n == 0:
            i=inp	
        i =sha256(i.encode('utf-8')).hexdigest()
        if n in [0,times-1]:
            print(n, "result ", pk_to_addr(i))
    return 'succeed' #i

print(rep_hash(NUMBER_OF_TIMES,input_))

