class Solution(object):
    def maximumWealth(self, accounts):
        ans = 0

        for row in accounts:
            ans = max(ans, sum(row))

        return ans