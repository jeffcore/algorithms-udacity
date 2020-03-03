# A RouteTrie will store our routes and their associated handlers
# see udacity for instructions
import collections

class RouteTrie:
    def __init__(self, root_node, handler):
        # Initialize the trie with an root node and a handler, this 
        #  is the root path or home page node
        self.root = root_node
        self.root_handler = handler

    def insert(self, path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current = self.root
        
        for p in path:
            current = current.children[p]
            
        current.is_end = True
        current.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current = self.root
        
        for p in path:        
            if p not in current.children:
                return None

            current = current.children[p]
    
        return current.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None, is_end=False):
        # Initialize the node with children as before, plus a handler
        self.children = collections.defaultdict(RouteTrieNode)      
        self.is_end = is_end
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        self.children[path] = RouteTrieNode()

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        root_node = RouteTrieNode(root_handler, True)

        self.route_trie = RouteTrie(root_node, root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        result =  self.route_trie.find(self.split_path(path))
        if result:
            return result
        else:
            return self.not_found_handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here      
        # path_parts =  path.split('/')  
 
        return [part for part in path.split('/') if part != '']

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/blog/article/hello", "hello handler") 
router.add_handler("/blog/article/hello2", "hello2 handler") 
router.add_handler("/blog/top", "top handler") 
# some lookups with the expected output
print("/ - ", router.lookup("/")) # should print 'root handler'
print("/home - ", router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print("/home/about - ", router.lookup("/home/about")) # should print 'about handler'
print("/home/about/ - ", router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print("/home/about/me - ", router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

## test of second route
print("/blog/article/hello - ", router.lookup("/blog/article/hello")) # should print 'hello handler' or None if you did not implement one
print("/blog/article/hello2 - ", router.lookup("/blog/article/hello2")) # should print 'hello2 handler' or None if you did not implement one
print("/blog/article/hello4 - ", router.lookup("/blog/article/hello4")) # should print 'not found handler' or None if you did not implement one

## two folders within route
print("/blog/top - ", router.lookup("/blog/top"))  # should print 'top handler' or None if you did not implement one

# empty node
router = Router("") 
print("/home - ", router.lookup("/home"))   # none

