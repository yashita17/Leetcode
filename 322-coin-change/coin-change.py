class Solution(object):
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]= 0
        for i in range(1,n+1):
            for j in range(1, amount+1):
                not_take = dp[i-1][j]
                if j >= coins[i-1]:
                    take = 1+ dp[i][j- coins[i-1]]
                else:
                    take = float('inf')
                dp[i][j] = min(take, not_take)
        if dp[n][amount] == float('inf'):
            return -1
        return dp[n][amount]
        

        