# Problem 1 - LRU Cache

I used a doubly linked list for the data structure to hold the key and value data. The most recent used item is at the front of the linked list and the tail is popped then capacity is full.  The time complexity to add a node, remove a node or pop a node from the tail are all O(1). 

I used a python dictionary as the cache data structure which consists of key:node, this is used to provide a O(1) lookup to find nodes in the doubly linked list. Adding and getting an element from the cache is O(1).

Space complexity is O(2n) for the linked list and dictionary.
