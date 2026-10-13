# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        seen = set()
        def solve(root):
            if root == None:
                return False
            diff = k - root.val
            if diff in seen:
                return True
            else:
                seen.add(root.val)
            return solve(root.left) or solve(root.right)
        return solve(root)
        