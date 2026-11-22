class Solution(object):
    def findLengthOfLCIS(self, nums):
        low = 0
        right = low + 1
        ans = count = 1
        while right != len(nums):
            if nums[right] > nums[right-1]:
                count = (right - low)+1
                right +=1
            else:
                low +=1
                right = low +1
            ans = max(ans, count)
        return ans

        