# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #return if the tree iss equivalent or not

        if not p and not q:
            return True
        if p and q and p.val == q.val:
            left_equal = self.isSameTree(p.left, q.left)
            right_equal = self.isSameTree(p.right,q.right)
            return left_equal and right_equal 
        else:
            return False