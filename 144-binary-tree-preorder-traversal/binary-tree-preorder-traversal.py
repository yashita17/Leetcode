# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            s = stack.pop()
            ans.append(s.val)
            if s.right:
                stack.append(s.right)
            if s.left:
                stack.append(s.left)
        return ans
        
        