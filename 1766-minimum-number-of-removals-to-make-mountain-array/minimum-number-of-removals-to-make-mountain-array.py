class Solution(object):
    def minimumMountainRemovals(self, nums):
        def ceiling(arr, target):
            low = 0
            high = len(arr)
            while low < high:
                mid = (low + high) //2
                if arr[mid] < target:
                    low = mid +1
                else:
                    high = mid
            return low
        left =[1]*(len(nums))
        tail = []
        for n in range(len(nums)):
            pos = ceiling(tail, nums[n])
            if pos == len(tail):
                tail.append(nums[n])
            else:
                tail[pos] = nums[n]
            left[n] = pos +1
        right =[1]*(len(nums))
        tail = []
        for i in range(len(nums)-1, -1, -1):
            # n = -nums[i]
            pos = ceiling(tail, nums[i])
            if pos == len(tail):
                tail.append(nums[i])
            else:
                tail[pos] = nums[i]
            right[i] = pos +1
        final_ans = 0
        for i in range(len(nums)):
            if left[i]>1 and right[i] > 1:
                ans = left[i] + right[i] -1
                final_ans = max(final_ans, ans)
        return (len(nums)- final_ans)

        