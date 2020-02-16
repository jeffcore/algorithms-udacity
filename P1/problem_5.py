## Blockchain ##
import hashlib

# TODO:  finish gmt timestamp

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()      

    def calc_hash(self):
      sha = hashlib.sha256()

      sha.update(self.data.encode('utf-8'))

      return sha.hexdigest()

class BlockChain:
    def __init__(self):
        self.tail = None

    def insert(self, data):
        new_block = Block(None, data, None)
        
        if self.tail == None:
            self.tail = new_block
        else:
            previous_tail = self.tail
            self.tail = new_block
            new_block.previous_hash = previous_tail
        
    def print(self):
        current = self.tail
        while current:
            print(current.data , ' ' , current.hash)
            current = current.previous_hash

# Test 1 - Block
block = Block(None, "testdata", None)
print(f'should have hash: 810ff2fb242a5dee4220f2cb0e6a519891fb67f2f828a6cab4ef8894633b1f50 Result {block.hash}')
assert('810ff2fb242a5dee4220f2cb0e6a519891fb67f2f828a6cab4ef8894633b1f50' == block.hash)

# Test 2 - Blockchain
bc = BlockChain()
bc.insert('bombtrack')
bc.insert('bombtrack 2')
bc.insert('bombtrack 3')
print(f'''Results Should look like this (tail to head):\nbombtrack 3   93b230233bf70deb04d6146a723aaab6be0ef60cb37a4dbaf57aede3f5429621 
bombtrack 2   4a2869f2995757581b6db2068087aa40080c211cbd83d4689eddaced2560a205
bombtrack   5ef78230e321d7fd562e6d517e4749a50d8f3ae65c9e7870ab8c645cded8e613''')

print('Results:')
bc.print()

# Test 3 - 
