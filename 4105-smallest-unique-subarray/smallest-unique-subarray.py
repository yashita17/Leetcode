class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        b1, b2 = 100019, 100043
        m1, m2 = 10**9 + 7, 10**9 + 9

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i in range(n):
            p1[i+1] = p1[i] * b1 % m1
            p2[i+1] = p2[i] * b2 % m2

            h1[i+1] = (h1[i] * b1 + nums[i]) % m1
            h2[i+1] = (h2[i] * b2 + nums[i]) % m2

        def check(k):
            freq = {}

            for i in range(n-k+1):
                x = (h1[i+k] - h1[i] * p1[k]) % m1
                y = (h2[i+k] - h2[i] * p2[k]) % m2

                key = (x, y)
                freq[key] = freq.get(key, 0) + 1

            return any(v == 1 for v in freq.values())

        low, high = 1, n

        while low < high:
            mid = (low + high) // 2

            if check(mid):
                high = mid
            else:
                low = mid + 1

        return low

        