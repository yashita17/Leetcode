# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        parent = {}
        def build(node, par = None):
            if  not node:
                return 
            parent[node] = par
            build(node.left, node)
            build(node.right, node)
        
        build(root)
        q = deque([(target, 0)])
        visited = {target}
        ans = []
        while q:
            size = len(q)
            for _ in range(size):
                node, d= q.popleft()
                if d==k:
                    ans.append(node.val)
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append((nei, d+1))
        return ans

            


        