class Solution(object):
    def thirdMax(self, nums):
        largest = float('-inf')
        second_largest = float('-inf')
        third_largest = float('-inf')
        for i in range(len(nums)):
            largest = max(largest, nums[i])
        nums_set = set(nums)
        if len(nums_set) <3:
            return largest
        for i in range(len(nums)):
            if(nums[i]!=largest):
                second_largest = max(nums[i], second_largest)
        for i in range(len(nums)):
            if(nums[i]!=largest and nums[i]!= second_largest):
                third_largest = max(nums[i], third_largest)
        
        return third_largest
        