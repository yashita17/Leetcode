# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        ans = self.solve(root)
        if ans == -1:
            return False
        else:
            return True
    def solve(self, root):
            if root == None:
                return 0
            lh = self.solve(root.left)
            if lh == -1:
                return -1
            rh = self.solve(root.right)
            if rh == -1:
                return -1
            if (abs(rh -lh)>1):
                return -1
            else:
                return max(lh, rh) +1