import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(data_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Usage example:
blockchain = Blockchain()

block1 = Block(1, datetime.datetime.now(), "Block 1 Data", "")
blockchain.add_block(block1)

block2 = Block(2, datetime.datetime.now(), "Block 2 Data", "")
blockchain.add_block(block2)

# Check if the blockchain is valid
print("Is blockchain valid?", blockchain.is_chain_valid())

# Modify data in a block to tamper with the chain
block1.data = "Modified Block 1 Data"

# Check if the modified blockchain is still valid
print("Is modified blockchain valid?", blockchain.is_chain_valid())
