# Problem 1 - Finding the Square Root of an Integer

## Decisions Behind Code

My first thought was to just return int(number**(1/2)) Then I figured there was a more difficult solution for this problem.

The second idea was to continually divide the number in half and search higher and lower numbers until the correct solution is found. I decide to use binary search as the foundation of the algorithm.

## Efficiency

### Time Complexity

Iteration:  O(log n) this process divides the number on each iteration.  
Time Complexity: O(log n) n is the value of input number  

### Space Complexity

Space Complexity: O(1) constant time as I am just reusing variables.  
