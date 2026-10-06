# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if root == None:
            return []
        ans = []
        qu = deque()
        qu.append(root)
        while qu:
            count = len(qu)
            level = []
            for i in range(count):
                q = qu.popleft()
                level.append(q.val)
                if q.left:
                    qu.append(q.left)
                if q.right:
                    qu.append(q.right)
            ans.append(level)
        ans.reverse()
        return ans
        