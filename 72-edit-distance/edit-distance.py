class Solution(object):
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = [[-1]*(n+1) for _ in range(m+1)]
        def solve(m,n):
            if m == 0:
                return n
            if n == 0:
                return m
            if dp[m][n] != -1:
                return dp[m][n]
            if word1[m-1] == word2[n-1]:
                return solve(m-1, n-1)
            dp[m][n] = 1+ min(solve(m,n-1), solve(m-1,n), solve(m-1,n-1))
            return dp[m][n]
        return solve(m,n)

        