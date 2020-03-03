# Problem 2 - Rotated Sorted Array

## Decisions Behind Code

I used binary search as the foundation of this algoritm. This gives the algorhtim the abilty to split the array in half and search of the half that is not rotated and reset the start and end index for the next iteration.

## Efficiency

### Time Complexity

Time complexity is O(log n) n is the number of elements in the list. The list is split in half on each iteration.

### Space Complexity

Constant space is O(n + 3) n is the number of elements in list and 3 is for the constant variables. Auxiliary space O(1) for the mid point variable.
Total space complexity is O(n + 4) which simplifies to O(n)
