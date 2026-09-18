class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        length = len(nums)
        def solve(arr):
            n = len(arr)
            if n == 1:
                return arr[0]
            dp = [0]*n
            dp[0] = arr[0]
            dp[1] = max(arr[1], arr[0])
            for i in range(2, n):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            return dp[n-1]
        return max(solve(nums[:-1]), solve(nums[1:]) )

        