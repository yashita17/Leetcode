class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prod = 1
        pre = [nums[0]]*n
        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i]
        for i in range(n-1,-1,-1):
            if i == 0:
                pre[0] = prod
            else:
                pre[i] = pre[i-1] * prod
                prod *= nums[i]
        return pre
            
        

        