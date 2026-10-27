class Solution(object):
    def maxSlidingWindow(self, nums, k):
        ans = []
        dq = deque()
        for i in range(k):
            ele = nums[i]
            while(dq and ele> nums[dq[-1]]):
                dq.pop()
            dq.append(i)
        for i in range(k, len(nums)):
            ans.append(nums[dq[0]])
            ele = nums[i]
            if i - dq[0] >= k:
                dq.popleft()
            while dq and ele> nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        ans.append(nums[dq[0]])
        return ans

        