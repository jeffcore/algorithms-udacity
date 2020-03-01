import collections
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.is_word = False
        self.children = collections.defaultdict(TrieNode)
              
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point       
        suf_list = []
      
        if self.is_word:
            suf_list.append(suffix)
                
        for char in self.children:
            print(char)
            new_suffix = suffix + char
            results = self.children[char].suffixes(new_suffix)
          
            print('results ' , results)
            suf_list.extend(results)
        
        return suf_list

class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current = self.root
        
        for char in word:
            current = current.children[char]
            
        current.is_word = True
        
    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current = self.root
        
        for char in prefix:
            if char not in current.children:
                return False

            current = current.children[char]
            
        return current
   

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    
prefixNode = MyTrie.find("a")
print(prefixNode.suffixes())
