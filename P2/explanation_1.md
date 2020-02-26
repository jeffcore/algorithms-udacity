# Problem 1 - Finding the Square Root of an Integer


## Decisions Behind Code
The first thought I had for the function was to just return  
int(number**(1/2))

I then figured there was a more difficult solution for this problem. The second thought was to continually divide the number in half and search higher and lower numbers until the correct solution is found. I decide to use binary search as the foundation of the algorithm. 

## Efficiency

### Time Complexity
Base Case - value 0 or 1 or negative:  O(1)   
Iteration:  O(log n) this process divides the number on each iteration.  
Time Complexity: O(log n) n is the value of input number  

### Space Complexity
Space Complexity: O(1) constant time as I am just reusing variables.  



