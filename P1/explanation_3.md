# Problem 3 - Huffman Encoding

## Data Structures Used:
1. Dictionary to store the character frequencies. Space Complexity O(n)
2. List of tuples to store the sorted dictionary. Space Complexity O(n)
3. Binary tree to store the huffman encoding. Space Complexity O(n) 
4. Dictionary to encode the character to bits map. Space Complexity O(n)

## Time Complexity:
1. Creating dictionary to store the character frequencies. O(n)
2. Sorting dictionary takes O(n log n)
3. Converting dictionary to list of tuples take O(n)
4. Creating binary tree takes O(n)
5. Build char map to bits is a recursive call takes O(n) 
6. Convert string to encoded bits O(n)
7. Decode bits to string take O(d*n) - length of character string times depth of tree

The worst case complexity of the entire algoritm is decoding the bits back to strings - O(d*n) This is because the characters are stored as leafs of the tree and the algorithm restarts at the top of the tree for each character.  The encoding process is O(n log n) for the sorting.