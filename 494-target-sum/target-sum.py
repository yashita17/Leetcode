class Solution(object):
    def findTargetSumWays(self, nums, target):
        n = len(nums)
        dp = {}

        def solve(i, curr_target):
            if i == n:
                if curr_target == target:
                    return 1
                else:
                    return 0
            if (i,curr_target) in dp:
                return dp[(i, curr_target)]
            plus = solve(i+1, curr_target + nums[i])
            minus = solve(i+1, curr_target - nums[i])

            dp[(i, curr_target)] = plus + minus
            return dp[(i, curr_target)]
        return solve(0, 0)