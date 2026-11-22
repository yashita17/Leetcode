class Solution(object):
    def lengthOfLIS(self, nums):
        def ceiling(tails, target):
            low, high = 0, len(tails)
            while low< high:
                mid = (low + high)//2
                if tails[mid] < target:
                    low = mid + 1
                else:
                    high = mid
            return low
        
        tails = []
        for num in nums:
            pos = ceiling(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        return len(tails)
        