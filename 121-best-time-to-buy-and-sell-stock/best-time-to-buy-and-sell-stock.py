class Solution(object):
    def maxProfit(self, prices):
        left = prices[0]
        max_profit = 0
        for right in prices:
            if left > right:
                left = right
            profit = right - left
            max_profit = max(max_profit, profit)
        
        return max_profit
        