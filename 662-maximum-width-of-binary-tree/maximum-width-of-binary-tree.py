# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        if root == None:
            return 0
        qu = deque([(root, 0)])
        ans = 0
        while qu:
            size = len(qu)
            first = qu[0][1]
            for _ in range(size):
                node, ind = qu.popleft()
                if node.left:
                    qu.append((node.left, 2*ind +1))
                if node.right:
                    qu.append((node.right, 2*ind +2))
            last = ind
            ans = max(ans, (last-first )+1)
        return ans


        
        