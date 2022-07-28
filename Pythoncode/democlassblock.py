import  hashlib
from hashlib import sha256
from re import A
import json

class demoBlock:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

        self.block_data = "-".join(transactions) + "-" + previous_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

    def fromDict(blockDict):
        block = demoBlock(blockDict['index'],blockDict['transactions'],blockDict['timestamp'],blockDict['previous_hash'],blockDict['nonce'])
        block.hash = blockDict['hash']
        return block

    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()    


'''
t1 = "1231"
t2 = "123141"

initial_block = demoBlock("Initial String" , [t1,t2])

print(initial_block.block_data)
print(initial_block.block_hash)


    def fromDict(blockDict):
        block = Block(blockDict['index'],blockDict['transactions'],blockDict['timestamp'],blockDict['previous_hash'],blockDict['nonce'])
        block.hash = blockDict['hash']
        return block

    def
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()
'''