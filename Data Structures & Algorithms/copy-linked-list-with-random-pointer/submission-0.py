"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #this initialization is important
        #we can have None pointers and those are legit values to consieder
        
        node_to_copy = {None:None}
        curr = head 

        while curr:
            copy_node = Node(curr.val)
            node_to_copy[curr] = copy_node
            curr = curr.next 
        
        curr = head
        while curr:
            copy_node = node_to_copy[curr]
            copy_node.next = node_to_copy[curr.next]
            copy_node.random = node_to_copy[curr.random]
            curr = curr.next

        return node_to_copy[head]
