# Problem 4 - Active Groups

I used a recursive call on every group and iteration on groups' children. The recrusive call is called for every group and has a compexity of O(n) and the iteration on a group's children is O(n). Entire complexity of the function is O(n) - number of total users and groups. 

The total space complexity for the call stack would be O(g) g being the total number of groups.  Final complexity is O(g)