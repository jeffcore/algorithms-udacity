### huffman encoding ###
import sys
from collections import deque

def huffman_encoding(data):
    if data == '':
        return 0, None

    # get sorted character frequencies as list of tuples 
    freq = get_frequencies(data)
    
    # build tree with only one item in frequency list
    if len(freq) == 1:
        character, value = freq.pop(0)
        tree = Tree(Node(value, None))
        tree.root.left = Node(value, character)
        bits = '0' * value
        return bits, tree

    # build tree
    while len(freq) > 1:
        item1, item1_value = freq.pop(0)
        item2, item2_value = freq.pop(0)
        new_node_value = item1_value + item2_value
        new_node = Node(new_node_value)

        #  build sub tree - check if any popped items are nodes
        if isinstance(item1, Node):           
            new_node.left = item1        
        else:            
            new_node.left = Node(item1_value, item1)
        
        if isinstance(item2, Node):            
            new_node.right = item2        
        else:
            new_node.right = Node(item2_value, item2)

        # find position to insert new sub tree based on value
        idx = len(freq)
        for i, f in enumerate(freq):                       
            if f[1] > new_node_value:
                idx = i
                break
                
        freq.insert(idx, (new_node, new_node_value))

    # assign first element in frequencies to tree
    huffman_tree = Tree(freq[0][0])  
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

    # sort frequencies
    freq = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1])}  
    # convert freqeunciies to list of tuples
    freq_list = [(k, v) for k, v in freq.items()] 

    return freq_list

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

class Tree:
    def __init__(self, root):
        self.root = root

# Test 1 - Entire process works
print('Test 1 - Entire process works')
a_great_sentence = "The bird is the word"
encoded_data, tree = huffman_encoding(a_great_sentence)
print(f'encoded data: {encoded_data} - should equal: 0110111011111100111000001010110000100011010011110111111010101011001010')
assert(encoded_data == '0110111011111100111000001010110000100011010011110111111010101011001010')
decoded_data = huffman_decoding(encoded_data, tree)
print(f'decoded data: {decoded_data} - should equal: The bird is the word')
assert(decoded_data == "The bird is the word")

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

