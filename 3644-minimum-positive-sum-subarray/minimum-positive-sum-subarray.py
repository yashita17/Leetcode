class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        mini = float('inf')
        for i in range(l, r+1):
            total = sum(nums[:i])
            if total >0:
                mini = min(mini, total)
            
            for j in range(i,n):
                total += nums[j] - nums[j-i]
                if total >0:
                    mini = min(mini, total)
        return mini if mini != float('inf') else -1

            


        
        