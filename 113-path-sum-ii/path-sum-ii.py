# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        ans = []
        path = []
        def solve(root, targetSum, path):
            if not root:
                return 
            path.append(root.val)
            targetSum -= root.val
            if not root.left and not root.right:
                if targetSum == 0:
                    ans.append(path[:])
            solve(root.left, targetSum, path)
            solve(root.right, targetSum, path)
            path.pop()
        solve(root, targetSum, path)
        return ans
        