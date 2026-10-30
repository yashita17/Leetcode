# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def amountOfTime(self, root, start):
        # self.res = 0
        # def dfs(root, start, dist):
        #     if not root:
        #         return 0
        #     if root.val == start:
        #         dist[0] = 0
        #         return 1
        #     ldist = [-1]
        #     rdist =[-1]
        #     lh = dfs(root.left, start, ldist)
        #     rh = dfs(root.right, start, rdist)

        #     if ldist[0] != -1:
        #         dist[0] = ldist[0] +1
        #         self.res = max(self.res, dist[0] + rh)
            
        #     elif rdist[0] != -1:
        #         dist[0] = rdist[0] +1
        #         self.res = max(self.res, dist[0] + lh)
        #     return max(lh, rh) +1
        # dist = [-1]
        # dfs(root, start, dist)
        # return self.res
        self.res = 0

        def dfs(root, start, dist):
            if not root:
                return 0

            if root.val == start:
                dist[0] = 0

                lh = dfs(root.left, start, [-1])
                rh = dfs(root.right, start, [-1])

                self.res = max(self.res, lh, rh)

                return max(lh, rh) + 1

            ldist = [-1]
            rdist = [-1]

            lh = dfs(root.left, start, ldist)
            rh = dfs(root.right, start, rdist)

            if ldist[0] != -1:
                dist[0] = ldist[0] + 1
                self.res = max(self.res, dist[0] + rh)

            elif rdist[0] != -1:
                dist[0] = rdist[0] + 1
                self.res = max(self.res, dist[0] + lh)

            return max(lh, rh) + 1

        dfs(root, start, [-1])
        return self.res

        