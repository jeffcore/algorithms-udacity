# Problem 1 - Finding the Square Root of an Integer

## Decisions Behind Code

My first idea for a solution was to use a recursive permutation algorithm. The time complexity of the recursive function and then finding the highest numbers would be greater than O(n log n). A required time complexity of O(n log n) usually means there is a sort algorithm involved. Once the list is sorted descending, a simple loop through the list splits the odd and even numbers into new numbers.

## Efficiency

### Time Complexity

The mergesort algorithm takes O(n log n) time - n for the number of elements in the list. The creation of the two number is done in linear time O(n). The time complexity is O(n log n) since 0(n) can be dropped.

### Space Complexity

The space complexity of mergsort is auxiliary space O(n) and constant space O(n) = O(2n)
The space complexity for the new numbers is O(1).
Total space compexity = O(2n+1)

Citations:
Found the trick for building the two max numbers. https://www.techiedelight.com/find-two-numbers-maximum-sum-array-digits/     