class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        for num in range (len(nums)):
            if nums[num] != 0:
                nums[num], nums[count]= nums[count], nums[num]
                count +=1
        return nums
                
        
        