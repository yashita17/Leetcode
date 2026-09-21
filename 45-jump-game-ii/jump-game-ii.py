class Solution(object):
    def jump(self, nums):
        n = len(nums)
        farthest = 0
        curr_end = 0
        jumps = 0
        for i in range(n-1):
            farthest = max(farthest, nums[i] + i)
            if i == curr_end:
                jumps +=1
                curr_end = farthest
        return jumps


            
        