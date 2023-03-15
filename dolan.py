import hashlib
import datetime


class Block:
    def _init_(self, data, previous_block_hash):
        self.timestamp = datetime.datetime.now()
        self.data = data
        self.previous_block_hash = previous_block_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp) + str(self.data) + \
            str(self.previous_block_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()


class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")

    def add_block(self, data):
        previous_block_hash = self.chain[-1].hash
        new_block = Block(data, previous_block_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_block_hash != previous_block.hash:
                return False
        return True
