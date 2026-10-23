class Solution(object):
    def sortPermutation(self, nums):
        res = -1
        for i in range(len(nums)):
            if nums[i] != i:
                res &= nums[i]
                if res == 0:
                    return 0
        return max(res, 0)
        