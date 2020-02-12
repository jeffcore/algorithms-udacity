import sys
from collections import deque

def huffman_encoding(data):
    freq = get_frequencies(data)
    print(freq)
    if len(freq) == 1:
        return 0

    while len(freq) > 1:
        item1 = freq.pop(0)
        item2 = freq.pop(0)
        item3 = item1[1] + item2[1]
        
        new_node = Node(item3)
        if isinstance(item1[0], Node):           
            new_node.left = item1[0]        
        else:            
            new_node.left = Node(item1[1], item1[0])
        
        if isinstance(item2[0], Node):            
            new_node.right = item2[0]        
        else:
            new_node.right = Node(item2[1], item2[0])

        idx = len(freq)
        for i, c in enumerate(freq):                       
            if c[1] > item3:
                idx = i
                break
                
        freq.insert(idx, (new_node, item3))
        print(freq)

       
    huffman_tree = Tree(freq[0][0])    
    encoding_map = huffman_encoder_map(huffman_tree.root)
    the_bits = huffman_string_to_bits(encoding_map, data)

    return the_bits, huffman_tree

def huffman_encoder_map(root, string = '', char_map={}):
    if not root:
        return

    if not root.left and not root.right:
        char_map[root.character] = string
    
    huffman_encoder_map(root.left, string + '0', char_map)
    huffman_encoder_map(root.right, string + '1', char_map)
    
    return char_map

def huffman_string_to_bits(char_map, data):
    output = ''
    for char in data:
        output += char_map[char]
    return output

def huffman_decoding(data,tree):
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

# used for printing out tree
class Queue():
    def __init__(self):
        self.q = deque()
        
    def enq(self,value):
        self.q.appendleft(value)
        
    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None
    
    def __len__(self):
        return len(self.q)
    
    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_________________\n" 
            s += "\n_________________\n".join([str(item) for item in self.q])
            s += "\n_________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"

class Tree:
    def __init__(self, root):
        self.root = root
    
    def print_tree_inorder(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.inorder_print(self.root, "")[:-1] # removes last - hypen
           
    def inorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:            
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def __repr__(self):
        level = 0
        q = Queue()
        visit_order = list()
        node = self.root
        q.enq( (node,level) )
        while(len(q) > 0):
            node, level = q.deq()
            if node == None:
                visit_order.append( ("<empty>", level))
                continue
            visit_order.append( (node, level) )
            if node.has_left_child():
                q.enq( (node.get_left_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

            if node.has_right_child():
                q.enq( (node.get_right_child(), level +1 ))
            else:
                q.enq( (None, level +1) )

        s = "Tree\n"
        previous_level = -1
        for i in range(len(visit_order)):
            node, level = visit_order[i]
            if level == previous_level:
                s += " | " + str(node) 
            else:
                s += "\n" + str(node)
                previous_level = level

        return s

if __name__ == "__main__":
  
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
 
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    print(tree)
    print('encoded data ' , encoded_data)
    print(tree.print_tree_inorder())