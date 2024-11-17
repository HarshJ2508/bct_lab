#pip install pycryptodome
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt(plain_text, key=None):
    """
    Encrypts data using AES-256-CBC
    Returns (key, iv, encrypted_data)
    """
    if key is None:
        # Generate a random 256-bit key
        key = get_random_bytes(32)
    
    # Create cipher object and generate random IV
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    
    # Pad and encrypt the data
    padded_data = pad(plain_text.encode(), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    
    return key, iv, encrypted_data

def aes_decrypt(encrypted_data, key, iv):
    """
    Decrypts AES-256-CBC encrypted data
    """
    # Create cipher object with the same IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    # Decrypt and unpad the data
    padded_data = cipher.decrypt(encrypted_data)
    original_data = unpad(padded_data, AES.block_size)
    
    return original_data.decode()


# Example usage
def main():
    # AES Example
    print("AES-256-CBC Example:")
    message = "Hello, this is a secret message!"
    
    # Encrypt
    key, iv, encrypted_data = aes_encrypt(message)
    print(f"Original message: {message}")
    print(f"Encrypted (base64): {base64.b64encode(encrypted_data).decode()}")
    
    # Decrypt
    decrypted_message = aes_decrypt(encrypted_data, key, iv)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()