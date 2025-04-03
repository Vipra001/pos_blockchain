import hashlib 
import json
import time
from collections import OrderedDict
class Block:
    def __init__(self,index,previous_hash,transactions,timestamp=None):
        self.index=index
        self.previous_hash=previous_hash
        self.transactions=transactions
        self.timestamp=timestamp or time.time()
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        block_data=json.dumps(
            OrderedDict({
                "index": self.index,
                "previous_hash": self.previous_hash,
                "transactions":self.transactions,
                "timestamp":self.timestamp
            }),
            sort_keys=True
        )
        return hashlib.sha256(block_data.encode()).hexdigest()
class Blockchain:
    def __init__(self):
        self.chain=[]
        self.create_genesis_block()
    def create_genesis_block(self):
        genesis_block = Block(0,"0",[],time.time())
        self.chain.append(genesis_block)
    def add_block(self,transactions):
        last_block = self.chain[-1]
        new_block =Block(len(self.chain),last_block.hash,transactions)
        self.chain.append(new_block)
    def print_chain(self):
        for block in self.chain:
            print(f"Index:{block.index},Hash:{block.hash},Prev Hash:{block.previous_hash},Transactions:{block.transactions}")
if __name__=="__main__":
    blockchain=Blockchain()
    blockchain.add_block(["Alice pays bob 5 BTC"])
    blockchain.add_block(["Bob pays charloe 2 BTC"])
    blockchain.print_chain()
    

