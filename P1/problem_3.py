### huffman encoding ###
import sys
import heapq
from collections import deque

def huffman_encoding(data):
    if data == '':
        return 0, None

    # get sorted character frequencies as list of tuples 
    freq_heap = get_frequencies(data)
    
    # build tree with only one item in frequency list
    if len(freq_heap) == 1:
        item = heapq.heappop(freq_heap)
        new_node = Node(item.value)
        new_node.left = item
        tree = Tree(new_node)       
        bits = '0' * item.value
        return bits, tree

    # build tree - this process creates a three node tree
    # top node is combined frequency of child -child nodes are item1 and item2
    # this new node is added back to heapq 
    # this repeats until freq_heap has only one item - tree is built
    while len(freq_heap) > 1:
        item1 = heapq.heappop(freq_heap)
        item2 = heapq.heappop(freq_heap)
        new_node_value = item1.value + item2.value
        
        #  build sub tree 
        new_node = Node(new_node_value)
        new_node.left = item1        
        new_node.right = item2        
        
        heapq.heappush(freq_heap, new_node)

    # assign first element in frequencies to tree
    top_node = heapq.heappop(freq_heap)
    huffman_tree = Tree(top_node)  

    # get map of bits to characters in tree  
    encoding_map = huffman_encoder_map(huffman_tree.root)
    
    # take encoder map to build bit string
    the_bits = huffman_string_to_bits(encoding_map, data)

    return the_bits, huffman_tree

# build map of bits to characters in tree 
def huffman_encoder_map(root, string = '', char_map={}):
    if not root:
        return

    if not root.left and not root.right:
        char_map[root.character] = string
    
    huffman_encoder_map(root.left, string + '0', char_map)
    huffman_encoder_map(root.right, string + '1', char_map)
    
    return char_map

# convert characters in string to bits
def huffman_string_to_bits(char_map, data):
    output = ''
    for char in data:
        output += char_map[char]
    return output

# decode a bit string back into character string
def huffman_decoding(data, tree):
    if data == '' or tree == None:
        return ''
    output = ''
    node = tree.root
    for bit in data:
        if bit == '0':
            node = node.left
        else:
            node = node.right
        
        if node.character:
            output += node.character
            node = tree.root

    return output

# build character frequencies from data
def get_frequencies(data): 
    freq = {}
    for c in data:
        if c in freq:
            freq[c] += 1            
        else:
            freq[c] = 1

    # convert freqeunciies to list of tuples
    freq_heap = []
    # add character frequencies to priority queue
    for k, v in freq.items():
        heapq.heappush(freq_heap, Node(v, k))    
        x
    print(freq_heap)
    return freq_heap

class Node():
    def __init__(self, value, character = None):
        self.value = value
        self.character = character
        self.left = None
        self.right = None

    def __str__(self):
       return f'value {self.value} char {self.character}'

    def __repr__(self):
       return f'value {self.value} char {self.character}'
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None
    
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def __lt__ (self, other):
        return self.value < other.value
    
    def __gt__ (self, other):
        return self.value > other.value



class Tree:
    def __init__(self, root):
        self.root = root

# Test 1 - Entire process works
print('Test 1 - Entire process works')
a_great_sentence = 'The quick brown fox jumps over the lazy dog'
encoded_data, tree = huffman_encoding(a_great_sentence)
print(f'encoded data: {encoded_data} - should equal: 10010111101010000110010001001111001011001100011011101101011000010111000101111010101100001011011000011110111011111000010111111101011011001110101111010100011101111100011100111000100110101010110100')
assert(encoded_data == '10010111101010000110010001001111001011001100011011101101011000010111000101111010101100001011011000011110111011111000010111111101011011001110101111010100011101111100011100111000100110101010110100')
decoded_data = huffman_decoding(encoded_data, tree)
print(f'decoded data: {decoded_data} - should equal: The quick brown fox jumps over the lazy dog')
assert(decoded_data == 'The quick brown fox jumps over the lazy dog')

# Test 2 - blank arguments
print('Test 2 - Blank arguments')
# encoding function
encoded_data, tree = huffman_encoding('')
print(f'encoding function should return: (0, None) Results: {huffman_encoding("")}')
assert(huffman_encoding('') == (0, None))
# decoding function
print(f'decoding function should return: "" Results: "{huffman_decoding("", None)}"')
assert(huffman_decoding('', None) == '')

# Test 3 -  String with with frequency length of one
print('Test 3 - String with with frequency length of one')
a_great_sentence = "TT"
encoded_data, tree = huffman_encoding(a_great_sentence)
print(f'encoded data: {encoded_data} - should equal: 00')
assert(encoded_data == '00')
decoded_data = huffman_decoding(encoded_data, tree)
print(f'decoded data: {decoded_data} - should equal: TT')
assert(decoded_data == "TT")

# Test 4 - Test from provided code
print('Test 4 - Test from provided code')
a_great_sentence = "The bird is the word"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

