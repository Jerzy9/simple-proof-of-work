import hashlib
import time

class Block():
    def __init__(self, index, timestamp, data, previous_hash = ""):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # data isin't stringfy
        return str(hashlib.sha256(str(str(self.index) +
                                      str(self.previous_hash) +
                                      str(self.timestamp) +
                                      str(self.data) +
                                      str(self.nonce)).encode()).hexdigest())

    def mine_block(self, difficulty):
        arr = [0] * difficulty

        while self.hash[0: difficulty] != "".join(map(str, arr)).replace(' ', ''):
            # print(self.hash, "".join(map(str, arr)).replace(' ', ''))
            self.nonce += 1
            self.hash = self.calculate_hash()

        print("Block mined: ", self.hash)


class Blockchain():
    def __init__(self):
        self.chain = [self.create_first_block()]
        self.diff = 4

    def create_first_block(self):
        return Block(0, time.time(), "First Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_last_block().hash
        new_block.mine_block(self.diff)

        self.chain.append(new_block)


blockchain = Blockchain()
print("Mining 1 block...")
blockchain.add_block(Block(1, time.time(), "amount 20B"))
print("Mining 2 block...")
blockchain.add_block(Block(2, time.time(), "amount 70B"))
print("Mining 3 block...")
blockchain.add_block(Block(3, time.time(), "amount 40B"))








