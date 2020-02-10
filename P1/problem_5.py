import hashlib

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


bc = BlockChain()

bc.insert('this is the bomb')
bc.insert('this is the bomb 2')
bc.insert('this is the bomb 3')
bc.print()