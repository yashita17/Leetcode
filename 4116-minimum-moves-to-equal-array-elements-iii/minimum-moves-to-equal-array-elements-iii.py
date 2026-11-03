class Solution(object):
    def minMoves(self, nums):
        m = max(nums)
        d = 0
        for i in range(len(nums)):
            d += m-nums[i]
        return d


        