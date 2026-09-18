class Solution(object):
    def climbStairs(self, n):
        dp = [-1]* (n+1)
        def solve(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if dp[n] != -1:
                return dp[n]
            dp[n] = solve(n-2) + solve(n-1)
            return dp[n]
        return solve(n)


        
        