class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        dp = [[0] * (amount +1) for _ in range(n+1)]
        def solve(amount):
            for i in range(n+1):
                dp[i][0] = 1
            for i in range(n-1, -1, -1):
                for j in range(1, amount + 1):
                    dp[i][j]= dp[i+1][j]
                    if j >= coins[i]:
                        dp[i][j] += dp[i][j- coins[i]]
            return dp[0][amount]
        return solve(amount)

        