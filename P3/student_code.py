import math
import heapq
class PriorityQueue:
    """
      Priority queue data structure. Each inserted item
      has a priority associated with it and the client is usually interested
      in quick retrieval of the lowest-priority item in the queue. 
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):       
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

    def __str__(self):
        return ' '.join(str(self.heap))

    
def distance(current, target):
    current_x, current_y = current
    target_x, target_y = target
    return math.sqrt((current_x - target_x)**2 + (current_y - target_y)**2) 

def shortest_path(M,start,goal):
    print("shortest path called")

    frontier = PriorityQueue()
    explored = set()
        
    if start == goal:
        return [start]
    
    frontier.push((start, [start], 0), 0)
    
    while not frontier.isEmpty():
        node, path, g_score = frontier.pop()
    
        if node not in explored:
            explored.add(node)
            
            if node == goal:                
                return path
            
            for child_node in M.roads[node]:                                
                new_path = path + [child_node]
                
                step_distance = distance(M.intersections[node], M.intersections[child_node])                
                goal_cost = distance(M.intersections[child_node], M.intersections[goal])                
                new_g_score = step_distance + g_score
                f_cost = new_g_score + goal_cost
                
                frontier.push((child_node, new_path, new_g_score), f_cost)
            
    return None


# Citations
# PriorityQueue class used from standford pacman project https://stanford.edu/~cpiech/cs221/homework/prog/pacman/pacman.html
 
