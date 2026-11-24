class Solution(object):
    def maxLength(self, nums):
        n = len(nums)
        ans = 0
        def gcd(a,b):
            while b:
                a,b = b, a%b
            return a
        for i in range(n):
            prod = 1
            l = 1
            g = 0
            for j in range(i,n):
                prod *= nums[j]
                g = gcd(g, nums[j])
                l = (l*nums[j])//gcd(l,nums[j])

                if prod == l*g:
                    ans = max(ans, j-i+1)
        return ans
        