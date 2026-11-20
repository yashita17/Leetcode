class Solution(object):
    def rob(self, nums):
        index = 0
        n = len(nums)   
        dp = [-1] * n
        def solve(nums, index, n):
            if index >= n:
                return 0
            if dp[index] != -1:
                return dp[index]
            op1 = nums[index] + solve(nums, index+2, n)
            op2 = 0 + solve(nums, index+1, n)
            ans = max(op1, op2)
            dp[index] = ans
            return dp[index]
        final_ans = solve(nums, index, n)
        return final_ans
        
        