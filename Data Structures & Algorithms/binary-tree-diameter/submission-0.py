# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        total_diameter = 0
        #get the diameter 

        def diameter(node):
            nonlocal total_diameter

            if not node:
                return (0,0)

            left_height, left_diameter = diameter(node.left)
            right_height, right_diameter = diameter(node.right)

            total_diameter = max(left_height+right_height, right_diameter, left_diameter)
            curr_height = 1+ max(left_height, right_height)
            return (curr_height, total_diameter)

        diameter(root)
        return total_diameter