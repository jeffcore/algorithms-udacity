Your paragraph should not be a detailed walkthrough of the code you provided, but provide your reasoning behind decisions made in the code. For example, why did you use that data structure? You also need to explain the efficiency (time and space) of your solution.

Efficiency

There is a clear and accurate statement of efficiency. There is an explanation that specifically mentions parts of the code that contribute to the overall efficiency.

Code Design

Explanation contains some discussion of design choices made in the code. Some examples include the choice of algorithm and data structure.
# Problem 6

## Decisions Behind Code
Just did an single traversal over the list and compared the each element to a min and max variable. 

## Efficiency

### Time Complexity
O(n) n being the length of list, for the single list traversal. All other operations were constant time O(1)  
Overal Time Complexity: O(n) n being the length of list

### Space Complexity 
Constant space is O(n) for the list, n being the number of elements in list. 

Auxilary Space: O(1) additional for min and max variables

Total Space Complexity: O(n) n being the number of elements in list. 