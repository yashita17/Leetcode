class Solution(object):
    def change(self, amount, coins):
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        def solve(amount, coins,index):
            if index >= n or amount < 0:
                return 0
            if amount == 0:
                return 1
            if dp[index][amount] != -1:
                return dp[index][amount]
            dp[index][amount] = solve(amount, coins, index+1) + solve(amount-coins[index], coins, index)
            return dp[index][amount]
        return solve(amount, coins, 0)
            
        