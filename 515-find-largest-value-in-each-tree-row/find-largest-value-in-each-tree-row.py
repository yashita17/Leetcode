# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        if root == None:
            return []
        ans = []
        qu = deque()
        qu.append(root)
        while qu:
            count = len(qu)
            level = []
            for _ in range(count):
                q = qu.popleft()
                level.append(q.val)
                if q.left:
                    qu.append(q.left)
                if q.right:
                    qu.append(q.right)
            ans.append(max(level))
        return ans
                    


        