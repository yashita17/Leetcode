class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [-1] * (n+1) 
        def solve(index):
            if index>=len(cost):
                return 0
            if dp[index] != -1:
                return dp[index]
            dp[index] = cost[index] + min(solve(index+1), solve(index + 2))
            return dp[index]
        return min(solve(0), solve(1))

        
        