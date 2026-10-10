# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        qu = deque()
        qu.append(root)
        ans = []
        while qu:
            size = len(qu)
            level = []
            for _ in range(size):
                q = qu.popleft()
                level.append(q.val)
                if q.left:
                    qu.append(q.left)
                if q.right:
                    qu.append(q.right)
            avg = float(sum(level))/float(len(level))
            ans.append(avg)
        return ans

        