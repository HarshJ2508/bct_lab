from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto import Random
import base64

def generate_key_pair(bits=2048):
    """
    Generate RSA key pair for digital signature
    """
    random_generator = Random.new().read
    key = RSA.generate(bits, random_generator)
    private_key = key
    public_key = key.publickey()
    return private_key, public_key

def create_signature(message, private_key):
    """
    Create digital signature for a message using private key
    """
    # Create hash of the message
    message_hash = SHA256.new(message.encode('utf-8'))
    
    # Create signature
    signature = pkcs1_15.new(private_key).sign(message_hash)
    
    return signature

def verify_signature(message, signature, public_key):
    """
    Verify digital signature using public key
    Returns True if signature is valid, False otherwise
    """
    # Create hash of the message
    message_hash = SHA256.new(message.encode('utf-8'))
    
    try:
        # Verify signature
        pkcs1_15.new(public_key).verify(message_hash, signature)
        return True
    except (ValueError, TypeError):
        return False

def save_keys_to_files(private_key, public_key, private_file='private_key.pem', public_file='public_key.pem'):
    """
    Save the keys to files
    """
    # Save private key
    with open(private_file, 'wb') as f:
        f.write(private_key.export_key('PEM'))
    
    # Save public key
    with open(public_file, 'wb') as f:
        f.write(public_key.export_key('PEM'))

def load_keys_from_files(private_file='private_key.pem', public_file='public_key.pem'):
    """
    Load keys from files
    """
    # Load private key
    with open(private_file, 'rb') as f:
        private_key = RSA.import_key(f.read())
    
    # Load public key
    with open(public_file, 'rb') as f:
        public_key = RSA.import_key(f.read())
    
    return private_key, public_key

def main():
    # Example usage of digital signatures
    
    # 1. Generate key pair
    print("Generating RSA key pair...")
    private_key, public_key = generate_key_pair()
    
    # Save keys (optional)
    save_keys_to_files(private_key, public_key)
    print("Keys saved to files: private_key.pem and public_key.pem")
    
    # 2. Original message
    message = "Hello, this message needs to be digitally signed!"
    print(f"\nOriginal Message: {message}")
    
    # 3. Create digital signature
    signature = create_signature(message, private_key)
    print(f"Digital Signature (base64): {base64.b64encode(signature).decode()}")
    
    # 4. Verify signature with correct message
    is_valid = verify_signature(message, signature, public_key)
    print(f"\nSignature Verification (correct message): {is_valid}")
    
    # 5. Try to verify with tampered message
    tampered_message = message + " [TAMPERED]"
    is_valid = verify_signature(tampered_message, signature, public_key)
    print(f"Signature Verification (tampered message): {is_valid}")
    
    # Example of loading keys from file
    print("\nLoading keys from files and verifying again...")
    loaded_private_key, loaded_public_key = load_keys_from_files()
    is_valid = verify_signature(message, signature, loaded_public_key)
    print(f"Signature Verification (using loaded keys): {is_valid}")

if __name__ == "__main__":
    main()