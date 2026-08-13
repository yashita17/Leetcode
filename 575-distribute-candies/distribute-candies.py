class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        candyType1 = set(candyType)
        k = len(candyType1)
        if k >= n/2:
            return n/2
        return k
        