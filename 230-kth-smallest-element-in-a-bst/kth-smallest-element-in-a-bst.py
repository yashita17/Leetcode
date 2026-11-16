# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        arr = []
        qu = deque([root])
        while qu:
            size = len(qu)
            for _ in range(size):
                q = qu.popleft()
                arr.append(q.val)
                if q.left:
                    qu.append(q.left)
                if q.right:
                    qu.append(q.right)
        arr.sort()
        ans = arr[k-1]
        return ans

        