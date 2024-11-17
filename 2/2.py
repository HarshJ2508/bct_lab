from Crypto.Hash import SHA256
import time
import random
import string

def get_hash(input_data):
    if isinstance(input_data, str):
        input_data = input_data.encode('utf-8')
    hash_object = SHA256.new(input_data)
    return hash_object.hexdigest()

def demonstrate_properties():
    # 1.Deterministic
    hash1 = get_hash("hello world")
    hash2 = get_hash("hello world")
    if(hash1 == hash2):
        print("Deterministic\n")
    else:
        print("Non Deterministic")
    
    # 2.Fixed length output
    inputs = ['a', 'ab', 'abc']
    for text in inputs:
        print(f"Length for text - {text}: {len(get_hash(text))}")
    print("\n")

    # 3.Avalanche Effect (small change in i/p results in large change in o/p)
    print(f"Hash 1: {get_hash("Hello, World!")}")
    print(f"Hash 2: {get_hash("Hello, World.")}")
    
    # 4.One-way Function (Pre-image resistance)
    target_hash = get_hash("secret message")
    attempts = 0
    start_time = time.time()
    while attempts < 100000:
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        if get_hash(random_str) == target_hash:
            print("Found a match!")
            break
        attempts += 1
    
    end_time = time.time()
    print(f"\nAttempted {attempts} random inputs in {end_time - start_time:.2f} seconds")
    print("Failed to find the original input (as expected)\n")

    # 5.Collision Resistance
    hashes_seen = set()
    attempts = 0
    start_time = time.time()
    while attempts < 100000:
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        hash_value = get_hash(random_str)
        
        if hash_value in hashes_seen:
            print("Found a collision! (This should be extremely rare)")
            break
            
        hashes_seen.add(hash_value)
        attempts += 1
    
    end_time = time.time()
    print(f"\nTested {attempts} random inputs in {end_time - start_time:.2f} seconds")
    print(f"Found no collisions among {len(hashes_seen)} unique hashes (as expected)\n")

if __name__ == "__main__":
    demonstrate_properties()