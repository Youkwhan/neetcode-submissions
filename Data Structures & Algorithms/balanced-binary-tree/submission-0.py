# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        #give a tree return if height balanced or false otherwise

        def dfs(node):
            if not node:
                return (0,True)
            left_height,left_bal = dfs(node.left)
            right_height, right_bal = dfs(node.right)
            is_balanced = left_bal and right_bal and abs(left_height-right_height) <= 1
            return (1+max(left_height, right_height), is_balanced)
        return dfs(root)[1]