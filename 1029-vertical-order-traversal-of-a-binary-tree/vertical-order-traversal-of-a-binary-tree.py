# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        d = {}
        def solve(root, hd, row):
            if root is None:
                return 
            solve(root.left, hd-1, row +1)
            if hd not in d:
                d[hd] = []
            d[hd].append((row, root.val))
            solve(root.right, hd +1, row+1)
        solve(root, 0, 0)
        ans = []
        for hd in sorted(d):
            d[hd].sort()
            ans.append([val for row, val in d[hd]])
        return ans
        

        