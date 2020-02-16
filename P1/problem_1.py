### LRU Cache ###

class Node:
    def __init__(self, key, value):
        self.key = value
        self.value = value
        self.next = None
        self.previous = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_tail(self):
        return self.tail

    def add(self, node):        
        if self.head == None:
            self.head = node
            self.tail = self.head
            node.previous = None
            return
            
        self.head.previous = node       
        node.next = self.head
        node.previous = None
        self.head = node

    # def move_to_top(self, node):
    #     if node.previous and node.next:
    #         node.previous.next = node.next                
    #         node.next.previous = node.previous
    #     elif node.next == None:            
    #         node.previous.next = None
    #         self.tail = node.previous

    #     self.prepend(node)
    
    def remove(self, node):
        if node.previous and node.next:
            node.previous.next = node.next                
            node.next.previous = node.previous
        elif node.next == None:            
            node.previous.next = None
            self.tail = node.previous

    # def pop(self):
    #     node = self.tail
    #     self.tail.previous.next = None
    #     self.tail = self.tail.previous        
    #     return node
    
    def __str__(self):
        list_str = ''
        current = self.head
        while current:            
            list_str += str(current.value) + ' '
            current = current.next
        
        return list_str[:-1]

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.link_list = DoublyLinkedList()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key in self.cache:
            node = self.cache[key]           
            self.link_list.remove(node)
            self.link_list.add(node)
            # self.link_list.move_to_top(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if len(self.cache) == self.capacity:            
            node_pop = self.link_list.get_tail()
            self.link_list.remove(node_pop)
            del self.cache[node_pop.key]

        node =  Node(key, value)
        self.cache[key] = node    
        self.link_list.add(node)

# Test 1 DoublyLinkedList
print('Test 1 : Doubly Linked List')
linked_list = DoublyLinkedList()
linked_list.add(Node(22, 7))
node_33 = Node(33, 8)
linked_list.add(node_33)
linked_list.add(Node(44, 9))
linked_list.add(Node(55, 6))
linked_list.add(Node(77, 5))
print(linked_list)
assert(str(linked_list)=='5 6 9 8 7')
node = linked_list.remove(node_33)
print(linked_list)
assert(str(linked_list)=='5 6 9 7')
assert(str(linked_list)=='5 6 9 7')
node_tail = linked_list.get_tail()
linked_list.remove(node_tail)
assert(str(linked_list)=='5 6 9')

# Test 2
print('Test 2 : LRU Cache')
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.link_list)
print(our_cache.get(1))      # returns 1
print(our_cache.get(2))      # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
print(our_cache.link_list)
our_cache.set(5, 5) 
print(our_cache.link_list)
our_cache.set(6, 6)
print(str(our_cache.link_list))
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
assert(str(our_cache.link_list)=='6 5 2 1 4')

# Test 3 
