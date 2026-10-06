# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root == None:
            return[]
        qu = deque()
        qu.append(root)
        ans = []
        while qu:
            size = len(qu)
            for i in range(size):
                q = qu.popleft()
                if i == (size -1):
                    ans.append(q.val)
                if q.left:
                    qu.append(q.left)
                if q.right:
                    qu.append(q.right)
        return ans

        
        