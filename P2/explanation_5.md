# Problem 5 - Autocomplete with Tries

## Decisions Behind Code

I used a resursive algoritm to find all the suffixes. The function builds each suffix before recusive call then build list of suffix when the stack is returned. The underlying data structure is a tree and a recursive algorithm is the best method to traverse a tree.

## Efficiency

### Time Complexity

The time complexity to find the search term is O(n \* m) n being total number of words and m being average length of words. The time complexity to find the suffixes O(n\*m) n being total number of words and m being average length of words. Total time complexity of O(2(n \* m)) -> O(n \* m)

### Space Complexity

The overall trie space is O(n \* m) n being total number of words and m being average length of words. The suffix auxilary space for the returned list is O(n \* m) n being total number of words and m being average length of words in the suffixes. The total space complexity is O(2(n + m)) simplified to O(n+m)
