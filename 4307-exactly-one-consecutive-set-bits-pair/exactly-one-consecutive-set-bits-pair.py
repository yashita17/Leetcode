class Solution(object):
    def consecutiveSetBits(self, n):
        x = n&(n>>1)
        return x !=0 and (x&(x-1)) == 0
        