class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range (len(nums)):
            comp = target -  nums[i]
            if comp in dict:
                return [dict[comp], i]
            
            dict[nums[i]] = i
        