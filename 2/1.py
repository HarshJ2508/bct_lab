#pip install pycryptodome
from Crypto.Hash import SHA256, MD5
hash_object = SHA256.new(b'13232U1 -> U2 | 1 BTC0000000000000000000000000000000000000000000000000000000000000000')
print(f"SHA256:{hash_object.hexdigest()}")

def calculate_md5(input_string):
    if isinstance(input_string, str):
        input_bytes = input_string.encode('utf-8')
    else:
        input_bytes = input_string
    md5_hash = MD5.new()
    md5_hash.update(input_bytes)
    return md5_hash.hexdigest()
print(f"MD5:{calculate_md5("hello world")}")