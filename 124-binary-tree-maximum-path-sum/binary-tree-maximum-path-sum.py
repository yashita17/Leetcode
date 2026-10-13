# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        self.Total = float('-inf')
        def path(root):
            if not root:
                return 0
            left = max(0, path(root.left))
            right = max(0, path(root.right))
            curr = root.val + left + right
            self.Total = max(self.Total, curr)
            return root.val + max(left, right)
        path(root)
        return self.Total
        