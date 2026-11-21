class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = [-1] * n
        def solve(ind):
            if ind >= n:
                return 0
            if dp[ind] != -1:
                return dp[ind]
            inc = nums[ind] + solve(ind +2)
            exc = 0 + solve(ind + 1)

            dp[ind] = max(inc, exc)
            return dp[ind]
        return solve(0)
        
        