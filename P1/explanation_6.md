# Linked List Union and Interection

## Union
I converted the first linked list to a set which takes O(n) where n is the length of the linked list. Then I compared all the elements in link list 2 to the linked list set. If the element was not in the set I appended it to link list 1. This process would be O(n) the length of second linked list and lookups would be O(1). Space complexity would be O(n) for the set.

## Intersection
I converted the first linked list to a set which takes O(n) where n is the length of the linked list. 
Then I compared all the elements in link list 2 to the elements in the set. If the element was in the set, I added it to a new link list and removed it from the set (this handles for duplicates).  Space complexity would be O(n+m) n for the number of elements in linked list 1 that are added to the new set and m for the new linked list for the results. 
