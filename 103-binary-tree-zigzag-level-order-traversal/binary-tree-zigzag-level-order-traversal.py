# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans = []
        qu = deque([root])
        flag = True
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
            if not flag:
                level.reverse()
            
            ans.append(level)
            flag = not flag
            
        return ans
        
        