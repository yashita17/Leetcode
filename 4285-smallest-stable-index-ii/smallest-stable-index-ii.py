class Solution(object):
    def firstStableIndex(self, nums, k):
        n = len(nums)
        prefix_sum = [0] * n
        suffix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1,n):
            prefix_sum[i] = max(prefix_sum[i-1], nums[i])
        
        suffix_sum[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            suffix_sum[i] = min(suffix_sum[i+1], nums[i])
        
        for i in range(n):
            if prefix_sum[i] - suffix_sum[i] <= k:
                return i
        return -1
        