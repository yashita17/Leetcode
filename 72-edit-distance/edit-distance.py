class Solution(object):
    def minDistance(self, word1, word2):
         m = len(word1)
         n = len(word2)
         dp = [[-1]*(n+1) for _ in range(m+1)]
         def solve(s1, s2, m, n):
            if m == 0:
                return n
            if n == 0:
                return m
            if dp[m][n]!= -1:
                return dp[m][n]
            if s1[m-1] == s2[n-1]:
                dp[m][n]= solve(s1, s2, m-1, n-1)
            else:
                remove = solve(s1, s2, m-1, n)
                insert = solve(s1, s2, m, n-1)
                replace = solve(s1, s2, m-1, n-1)
                dp[m][n]= 1 + min(remove, insert, replace)
            return dp[m][n]
         return solve(word1, word2, m ,n)


        