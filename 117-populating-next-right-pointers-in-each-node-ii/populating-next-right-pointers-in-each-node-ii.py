"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        if not root:
            return None
        qu = deque([root])
        while qu:
            size = len(qu)
            for i in range(size):
                q = qu.popleft()
                if i< size-1:
                    q.next = qu[0]
                if q.left:
                    qu.append(q.left)
                if q.right:
                    qu.append(q.right)
        return root


        