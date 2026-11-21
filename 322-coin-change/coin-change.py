class Solution(object):
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]

        def solve(ind, amount):
            if ind>= n or amount<0:
                return float('inf')
            if amount == 0:
                return 0
            if dp[ind][amount] != -1:
                return dp[ind][amount]
            ans = min(1+solve(ind, amount-coins[ind]), solve(ind+1, amount))
            dp[ind][amount] = ans
            return dp[ind][amount]
        if solve(0,amount) == float('inf'):
            return -1
        else:
            return solve(0, amount)
            
        
        