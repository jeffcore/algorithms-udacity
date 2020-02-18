## link list union intersection ##

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        out_string = ""
        while current:
            out_string += str(current.value)
            if current.next:
                out_string +=  " -> "
            current = current.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def to_list(self):
        the_list = []
        
        current = self.head

        while current:
            the_list.append(current.value)
            current = current.next
        
        return the_list

def union(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        print('you did not provide two linked lists')
        return None

    list1 = set(llist_1.to_list())
    list2 = set(llist_2.to_list())

    u_list = list1.union(list2)

    return u_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    if llist_1 == None or llist_2 == None:
        print('you did not provide two linked lists')
        return None

    list1 = set(llist_1.to_list())
    list2 = set(llist_2.to_list())

    u_list = list1.intersection(list2)

    if len(u_list):
        return u_list
    else:
        return None

# test prep
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

# Test case 1 - Test Union
print(f'union of lists should be {{32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21}} code results {union(linked_list_1,linked_list_2)}')
assert({32, 65, 2, 35, 3, 4, 6, 1, 9, 11, 21} == union(linked_list_1,linked_list_2))

# Test case 2 - Test Intersection
print(f'union of lists should be {{4, 21, 6}} code results {intersection(linked_list_1,linked_list_2)}')
assert({4, 21, 6} == intersection(linked_list_1,linked_list_2))

# Test case 3 - Linked list Blank
print(f'testing union function - should return: None, returned: {union(None,linked_list_2)} ')
print(f'testing intersection function - should return: None, returned: {intersection(None,linked_list_2)} ')
assert(None == union(None,linked_list_2))
assert(None == intersection(None,linked_list_2))

# Test case 4 - Node Class
node = Node(8)
print(f'node should have a value of 8 - result {node.value}')
assert(8 == node.value)

# Test case 5 - Linked List
ll = LinkedList()
ll.append(Node(8))
ll.append(Node(9))
print(f'linked list should look like this: 8 -> 9 Result: {ll}')
print(f'linked list to list should look like this: [8, 9] Result: {ll.to_list()}')
assert('8 -> 9' == str(ll))
assert('[8, 9]' == str(ll.to_list()))


# Provided test cases
print('Provided test cases:')
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))