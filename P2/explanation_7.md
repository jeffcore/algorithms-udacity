# Problem 5 - Autocomplete with Tries

## Decisions Behind Code
The starter code clearly suggested that we use a Trie data structure :)

## Efficiency

### Time Complexity

Insert time complexity of  O(n) n being total number of paths/nodes in trie. The time complexity to find the final path is O(n) n being total number of paths/nodes in trie. The time complexity to find the suffixes is  O(n) n being total number of paths/nodes in trie. Total time complexity of O(2n) -> O(n)

### Space Complexity

The overall trie space is O(n) n total path/nodes in the trie. The suffix auxilary space for the returned list is O(m) m being the total number of suffixes found. The total space complexity is O(n + m)
