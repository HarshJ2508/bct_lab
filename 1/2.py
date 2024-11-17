from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import base64

def generate_rsa_keys(bits=2048):
    """
    Generates RSA key pair
    Returns (private_key, public_key)
    """
    # Generate random numbers
    random_generator = Random.new().read
    
    # Generate key pair
    private_key = RSA.generate(bits, random_generator)
    public_key = private_key.publickey()
    
    return private_key, public_key

def rsa_encrypt(message, public_key):
    """
    Encrypts message using RSA public key
    """
    # Create cipher object
    cipher = PKCS1_OAEP.new(public_key)
    
    # Encrypt the message
    encrypted_data = cipher.encrypt(message.encode())
    
    return encrypted_data

def rsa_decrypt(encrypted_data, private_key):
    """
    Decrypts message using RSA private key
    """
    # Create cipher object
    cipher = PKCS1_OAEP.new(private_key)
    
    # Decrypt the message
    decrypted_data = cipher.decrypt(encrypted_data)
    
    return decrypted_data.decode()

def save_keys_to_file(private_key, public_key, private_file='private.pem', public_file='public.pem'):
    """
    Saves the RSA keys to files
    """
    # Save private key
    with open(private_file, 'wb') as f:
        f.write(private_key.export_key('PEM'))
    
    # Save public key
    with open(public_file, 'wb') as f:
        f.write(public_key.export_key('PEM'))

def load_keys_from_file(private_file='private.pem', public_file='public.pem'):
    """
    Loads RSA keys from files
    """
    # Load private key
    with open(private_file, 'rb') as f:
        private_key = RSA.import_key(f.read())
    
    # Load public key
    with open(public_file, 'rb') as f:
        public_key = RSA.import_key(f.read())
    
    return private_key, public_key

def main():
    # RSA Example
    print("\nRSA Example:")
    
    # Generate keys
    private_key, public_key = generate_rsa_keys()
    
    # Save keys to file (optional)
    save_keys_to_file(private_key, public_key)
    
    # Encrypt message
    message = "This is a secret RSA message!"
    encrypted_data = rsa_encrypt(message, public_key)
    print(f"Original message: {message}")
    print(f"Encrypted (base64): {base64.b64encode(encrypted_data).decode()}")
    
    # Decrypt message
    decrypted_message = rsa_decrypt(encrypted_data, private_key)
    print(f"Decrypted message: {decrypted_message}")

if __name__ == '__main__':
    main()