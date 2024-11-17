#pip install pymerkle
from pymerkle import InmemoryTree as MerkleTree
from pymerkle import verify_inclusion, verify_consistency
import json
from datetime import datetime
import hashlib

def create_sample_transactions():
    return [
        {
            "from": "Alice",
            "to": "Bob",
            "amount": 100,
            "timestamp": str(datetime.now())
        },
        {
            "from": "Bob",
            "to": "Charlie",
            "amount": 50,
            "timestamp": str(datetime.now())
        },
        {
            "from": "Charlie",
            "to": "David",
            "amount": 75,
            "timestamp": str(datetime.now())
        },
        {
            "from": "David",
            "to": "Alice",
            "amount": 25,
            "timestamp": str(datetime.now())
        }
    ]
    

def hash_transaction(transaction):
    tx_string = json.dumps(transaction, sort_keys=True)
    return tx_string.encode() 

def main():
    transactions = create_sample_transactions()
    
    merkle_tree = MerkleTree(algorithm='sha256')
    
    leaf_indices = []
    print("\n1.Original Transactions:")
    for i, tx in enumerate(transactions):
        print(f"\nTransaction {i + 1}:")
        print(json.dumps(tx, indent=2))
        index = merkle_tree.append_entry(hash_transaction(tx))
        leaf_indices.append(index)
        
    print("\n2. Merkle Root:")
    print(merkle_tree.get_state())
    
    print("\n3. Tree Size:")
    print(f"Number of leaves: {merkle_tree.get_size()}")
    
    
    print("\n4. Tampering Detection:")
    tampered_transactions = transactions.copy()
    tampered_transactions[0]['amount'] = 999  # Change amount
    
    tampered_tree = MerkleTree(algorithm='sha256')
    for tx in tampered_transactions:
        tampered_tree.append_entry(hash_transaction(tx))
    
    print("\nOriginal Merkle Root:")
    print(merkle_tree.get_state())
    print("\nTampered Merkle Root:")
    print(tampered_tree.get_state())
    print("\nRoots are different, indicating tampering!")
    
if __name__ == "__main__":
    main()