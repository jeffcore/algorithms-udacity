# Problem 2 - Find Files Recursive 

I used a recursive function to search each sub directory and iteration to search files in each subdirectory.  The time complexity is O(n)- n being the total number of files and directories in the entire directory tree. 

The total space complexity is O(n) - n for the number of directories in the directory tree. The call stack will grow by 1 for every directory found. O(m) - m for the total number of files in directory tree, worst case is all files are the same. 
Final space complexity O(n+m) 