# Problem 3 - Huffman Encoding

## Design
I used a combination of dictionaries, a python heapq and a binary tree to solve this problem. 
The dictionaries is used to map a key to a value, used in the character frequencies and bits to character map data structure. This enabled the fasts lookup for elements in dictionaries O(1). 

The python heapq is used to hold the character frequencies nodes as the huffman tree is built. The process of building a huffman tree is the repetitive actions of pop and pushing nodes based on priority. The heapq was build specifically for this and provides O(log n) on both actions.

The huffman tree is built with binary tree. This provides the fastest data structure to traverse and build the bits to character encoding map and also in decoding.

## Time Complexity:
### Encoding
1. Creating dictionary to store the character frequencies. O(n)
2. Sorting dictionary takes O(n log n)
3. Converting dictionary to heapq takes O(log n) for heapq.heappush()
4. Creating binary tree takes O(log n) for heapq.heappop()
5. Build char map to bits is a recursive call takes O(n+m) - n being the number of charachters in tree, m being number of parent nodes that are the addition of child nodes
6. Convert string to encoded bits O(n) - linear time just iterating over characters in string and accessing bits map

The worst case complexity encoding process is O(n log n) for the sorting.

### Decoding
1. Decode bits to string takes O(n) - length of decoded string

The worst case complexity of the decoding algoritm - O(n) 

Overall Complexity: O(n log n)

## Space Complexity:
### Encoding
1. Dictionary to store the character frequencies. Space Complexity O(n) - n is the number of elements in frequency dictionary
2. I create nodes from the frequency dictionary and added them to a python heapq. Space Complexity O(n) - n is the number of elements in frequency dictionary
3. Binary tree to store the huffman encoding. Space Complexity O(n+m) - n is the number of elements the heapq, m is the total number of parent nodes that are the addition of child nodes
4. Dictionary to encode the character to bits map. Space Complexity O(n) - n is the number of elements frequency dictionary

### Decoding
No data structures are created during the decoding process. It uses the existing huffman tree and encoded data.

