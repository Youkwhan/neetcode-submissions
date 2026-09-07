# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        1, l1, 2
        2, 1,
        3, l1, 1
        4, 1



        """
        if not root: return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left, right)