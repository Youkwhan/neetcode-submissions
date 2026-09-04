# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        EACH NODE:
        left
        print
        right
        """
        def inorder(root,res):
            if not root:
                return None
            inorder(root.left,res)
            res.append(root.val)
            inorder(root.right,res)

        res = []
        inorder(root,res)
        return res