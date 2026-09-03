# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #given the roots of two binary trees root and subroot 
        #return true if there is a subtree of root 
        if not subRoot:
            return True 
        if not root:
            return False
        
        if self.is_same_tree(root,subRoot):
            return True 
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        



    def is_same_tree(self, node1,node2):
        if not node1 and not node2:
            return True 
        elif node1 and node2 and node1.val == node2.val:
            return self.is_same_tree(node1.left,node2.left) and self.is_same_tree(node1.right, node2.right)
        else:
            return False 