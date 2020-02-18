# Problem 3 - Huffman Encoding

# todo review complexity of tranversing entier binary tree
# todo review time of sort function

## Data Structures Used:
1. dictionary to store the character frequencies. Space Complexity O(N)
2. list of tuples to store the sorted dictionary. Space Complexity O(N)
3. binary tree to store the huffman encoding. Space Complexity O(N) 
4. dictionary to encode the character to bits map. Space Complexity O(d*N)


I sorted the dictionary and converted it to a list of tuples. 
I used a binary tree to store the huffman encoding.
I used a dictionary to encode the character to bits map

## Time Complexity:
1. creating dictionary takes O(N)
2. sorting list takes O(N log N)
3. converting dictionary to list of tuples take O(N)
4. creating binary tree takes O(N)
5. build char map to bits is a recursive call takes O(N) 
6. convert string to encoded bits O(N)
7. decode bits to string take O(d*N) - length of character string times depth of tree

The worst case complexity of the entire algoritm is decoding the bits back to strings - O(d*N) This is because the characters are stored as leafs of the tree and the algorithm restarts at the top of the tree as decodes the bits.