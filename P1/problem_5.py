## Blockchain ##
import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = str(timestamp)
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()      

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode('utf-8'))
        sha.update(self.timestamp.encode('utf-8'))
        if self.previous_hash:
            sha.update(self.previous_hash.encode('utf-8'))

        return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.tail = None

    def insert(self, data):
        new_block = Block(datetime.utcnow().timestamp(), data, None)
        
        if self.tail == None:
            self.tail = new_block
        else:
            previous_tail = self.tail
            self.tail = new_block
            new_block.previous_hash = previous_tail

    def print(self):
        current = self.tail
        while current:
            print('Block ' , current.data)
            print('Timestamp: '  , current.timestamp )
            print('Hash:  ' , current.hash)
            if current.previous_hash:
                print('Previous Hash:  ' , current.previous_hash.hash , '\n')
            else:
                print('Previous Hash: None  \n')
            current = current.previous_hash

# Test 1 - Creation of Block and Hash
block = Block(1581877632.248518, "testdata", None)
print(f'should have a successful hash: {block.hash}')
assert('9eaf44d0a9f68275a7339a245b5682c51081247c77142acb59a264a7f25f9ceb' == block.hash)
block2 =  Block(1581877632.248518, "testdata", block.hash)
print(f'should have a successful hash: {block2.hash}')
assert('12ad9fba49724be9df0bf4550e8b70a28310f9a14a3aa7af078291990c526a3b' == block2.hash)

# Test 2 - Creation of Blockchain
bc = BlockChain()
bc.insert('block 1')
bc.insert('block 2')
bc.insert('block 3')

print('Results should have three blocks:')
bc.print()

assert(bc.tail.data == 'block 3')
assert(bc.tail.previous_hash.data == 'block 2')
assert(bc.tail.previous_hash.previous_hash.data == 'block 1')

# Test 3 - Check last block has none previous hash
block1 = bc.tail.previous_hash.previous_hash
assert(block1.previous_hash == None)