# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        parent = {}
        start_node = [None]
        def build(node, par=None):
            if not node:
                return
            parent[node] = par
            if node.val == start:
                start_node[0] = node
            build(node.left, node)
            build(node.right, node)
        build(root)

        q = deque([start_node[0]])
        visited = {start_node[0]}
        time = -1
        while q:
            size = len(q)
            time +=1
            for _ in range(size):
                node = q.popleft()
                for nei in (node.left, node.right, parent[node]):
                    if nei and nei not in visited:
                        visited.add(nei)
                        q.append(nei)
        return time

        