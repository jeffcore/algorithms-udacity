# Linked List Union and Interection

## Union
I converted the first linked list to a set which takes O(n). Then compared all the elements in link list 2 to the linked list set. If the element was not in the set I appended it to link list 1. This process would be O(n) the length of second linked list and lookups would be O(1). Space complexity would be O(n) for the set.

## Intersection
I converted both link lists to sets O(n) time. Then I used the intersection set functions which take O(n) - n being the length of the smaller set. Last, I popped all elements out of the intersection set and created a new linked list in O(n) time.  Space complexity would be O(3n) for linked list sets and intersection set.
