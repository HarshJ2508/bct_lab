1. AES-256-CBC Symmetric Encryption using OpenSSL:

# Generate a 256-bit (32 bytes) random key
openssl rand -base64 32 > aes_key.txt

# Encrypt a file using AES-256-CBC
openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.bin -kfile aes_key.txt

# Decrypt the file
openssl enc -aes-256-cbc -d -in encrypted.bin -out decrypted.txt -kfile aes_key.txt

# Alternative: Encrypt using password instead of key file
openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.bin -pass pass:"your_password"

# Decrypt using password
openssl enc -aes-256-cbc -d -in encrypted.bin -out decrypted.txt -pass pass:"your_password"

2. RSA Key Generation and Asymmetric Encryption:
# Generate private key (2048 bits)
openssl genrsa -out private_key.pem 2048

# Extract public key from private key
openssl rsa -in private_key.pem -pubout -out public_key.pem

# Encrypt file using public key
openssl rsautl -encrypt -pubin -inkey public_key.pem -in plaintext.txt -out encrypted.bin

# Decrypt file using private key
openssl rsautl -decrypt -inkey private_key.pem -in encrypted.bin -out decrypted.txt

# Generate private key with passphrase protection
openssl genrsa -aes256 -out private_key_encrypted.pem 2048

# Remove passphrase from private key (if needed)
openssl rsa -in private_key_encrypted.pem -out private_key_decrypted.pem

3. Digital Signatures using RSA and SHA:
# Create a digital signature using SHA256
openssl dgst -sha256 -sign private_key.pem -out signature.bin document.txt

# Verify the signature
openssl dgst -sha256 -verify public_key.pem -signature signature.bin document.txt

# Alternative: Create detached signature with SHA512
openssl dgst -sha512 -sign private_key.pem -out signature.bin document.txt

# Verify SHA512 signature
openssl dgst -sha512 -verify public_key.pem -signature signature.bin document.txt

# Create signature in base64 format
openssl dgst -sha256 -sign private_key.pem -out signature.bin document.txt
base64 signature.bin > signature.base64