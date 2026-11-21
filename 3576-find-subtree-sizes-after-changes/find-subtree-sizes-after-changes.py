class Solution(object):
    def findSubtreeSizes(self, parent, s):
        n = len(parent)

        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_children = [[] for _ in range(n)]
        last = {}

        def build(node):
            ch = s[node]

            old = last.get(ch, -1)

            if old == -1:
                p = parent[node]
            else:
                p = old

            if p != -1:
                new_children[p].append(node)

            last[ch] = node

            for child in children[node]:
                build(child)

            if old == -1:
                del last[ch]
            else:
                last[ch] = old

        build(0)

        ans = [0] * n

        def dfs(node):
            ans[node] = 1

            for child in new_children[node]:
                ans[node] += dfs(child)

            return ans[node]

        dfs(0)
        return ans
        