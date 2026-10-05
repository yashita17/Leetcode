class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        tail = []
        for i in nums:
            pos = self.ciel(tail, i)
            if pos == len(tail):
                tail.append(i)
            else:
                tail[pos] = i
        return len(tail)
    def ciel(self, arr, target):
        low = 0
        high = len(arr)
        while low < high:
            mid = (low + high)//2
            if arr[mid] < target:
                low = mid +1
            else:
                high = mid
        return low

            