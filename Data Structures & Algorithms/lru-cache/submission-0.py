class Node:

    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next 

class LRUCache:

    #LRU <------> MRU#
    def __init__(self, capacity: int):
        self.LRU = Node(0,0)
        self.MRU = Node(0,0)
        self.capacity = capacity
        #key -key value - (key, Node)
        self.hashmap = {}

        self.LRU.next = self.MRU
        self.MRU.prev = self.LRU 
        

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1 
        node = self.hashmap[key]
        self.remove(node)
        self.insert(node)
        return node.value
    

    def put(self, key: int, value: int) -> None:
        #check capcity and if at capcity remove 
        if key in self.hashmap:
            self.remove(self.hashmap[key])
        new_node = Node(key,value)
        self.insert(new_node)
        self.hashmap[key] = new_node


        if len(self.hashmap) > self.capacity:
            lru = self.LRU.next
            self.remove(lru)
            del self.hashmap[lru.key]
        

        

    #remove a node
    def remove(self, node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev 

    # insert a node to the MRU side
    def insert(self, node) -> None:
        prev = self.MRU.prev 

        node.prev = prev
        prev.next = node

        node.next = self.MRU
        self.MRU.prev = node 

#LRU cache

#so if we have a cache we want to kick out the LEAST recently used
#so if we have something used we want to immediately pop it to front

#O(1) -- either a DeQUE or a Doubly linked list 
#makes sense to do a double linked list 

#LEFT LRU side 
#RIGHT MRU side
#store a dictionary with key to Node
#we can check the size of dictionary and decide to kick out
#whenever we use put 

#


