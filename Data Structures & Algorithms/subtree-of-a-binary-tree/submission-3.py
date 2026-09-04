# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        true if subtree exist in tree

        PREORDER 
        print
        left
        right

        SUBPROBLEM:
        - TRAVERSAL
        - EDGE CASE what do we want to return for each from bottom to top. (PREORDER)
        """
        # edge cases of when this wont work
        # BUILDING on the edge cases instead of seperate conditions.
        if subRoot is None:
            return True # a empty subtree is always a match
        if root is None: 
            return False # if above is not empty, then a none empty root is not same.

        # if null cases pass 
        if self.is_same_tree(root, subRoot):
            return True

        # To traverse two trees we use once for left one for right
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def is_same_tree(self, node1, node2): #Return Bool
        if not node1 and not node2: #base 
            return True
        elif node1 and node2 and node1.val == node2.val:# travese
            return self.is_same_tree(node1.left, node2.left) and self.is_same_tree(node1.right, node2.right)
        else: # not matrch
            return False
        