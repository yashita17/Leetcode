# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        def invert(root):
            if not root:
                return
            left = root.left
            right = root.right
            root.left = right
            root.right = left
            self.invertTree(root.left)
            self.invertTree(root.right)
        invert(root)
        return root



        