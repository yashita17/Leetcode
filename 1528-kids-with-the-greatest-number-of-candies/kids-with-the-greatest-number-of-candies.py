class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        m = max(candies)
        ans = []

        for x in candies:
            ans.append(x + extraCandies >= m)

        return ans
        