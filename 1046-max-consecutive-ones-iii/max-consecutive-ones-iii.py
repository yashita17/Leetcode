class Solution(object):
    def longestOnes(self, nums, k):
        j=0
        max_count = 0
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes +=1
            while zeroes> k:
                if nums[j] == 0:
                    zeroes -= 1
                j +=1
            max_count = max(max_count, i-j+1)
        return max_count