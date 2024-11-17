# pip install pycryptodome
from Crypto.Hash import SHA256

class Block:
    def __init__(self, txn, block_no, hash, prev_hash, nonce):
        self.txn = txn
        self.next = None
        self.block_no = block_no
        self.hash = hash    
        self.prev_hash = prev_hash
        self.nonce = nonce
    
class BlockChain:
    block_no = 1

    def __init__(self):
        self.block = None
        self.prev_hash_string = "0000000000000000000000000000000000000000000000000000000000000000"  
    
    def append(self, txn, hash, prev_hash, nonce):
        new_block = Block(txn, BlockChain.block_no, hash, prev_hash, nonce)

        if not self.block:
            self.block = new_block
            return
        
        last_block = self.block
        while last_block.next:
            last_block = last_block.next

        last_block.next = new_block
        BlockChain.block_no += 1  #

    def display(self):
        curr_block = self.block
        if not curr_block:
            print("No blocks added in blockchain")

        while curr_block:
            print(f"Block No.: {curr_block.block_no}")
            print(f"Nonce: {curr_block.nonce}")
            print(f"Transaction: {curr_block.txn}")
            print(f"Prev Hash: {curr_block.prev_hash}")
            print(f"Hash: {curr_block.hash}")
            curr_block = curr_block.next

blockchain = BlockChain()

def add_block():
    txn = input("Enter txn: ")
    nonce = 0
    prev_hash_string = blockchain.prev_hash_string  
    while True:
        block_details = str(BlockChain.block_no) + str(nonce) + txn + prev_hash_string
        hash_object = SHA256.new(block_details.encode('utf-8'))
        hash_string = hash_object.hexdigest()
        
        for i in range(4):
            if hash_string[i] == '0':
                continue
            else:
                break 
        if i == 3 and hash_string[i] == '0':  
            break
        nonce += 1

    print(f"Hash with first 4 zeros: {hash_string}, with nonce as {nonce}")
    blockchain.append(txn, hash_string, prev_hash_string, nonce)
    blockchain.prev_hash_string = hash_string

def get_blockchain():
    blockchain.display()

while True:
    choice = int(input("\n1. Get blockchain details\n2. Add Block to blockchain\n3. Exit\nEnter your choice: "))
    
    if choice == 3:
        break
    elif choice == 1:
        get_blockchain()
    elif choice == 2:
        add_block()
