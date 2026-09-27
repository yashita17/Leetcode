class Solution(object):
    def isPowerOfTwo(self, n):
        r =0
        if n <=0:
            return False
        elif n == 1:
           return True
        else:
            while(n!=1 and r!=1):
                r = n%2 
                n = n//2
            if (n==1 and r==0):
                return True
            else:
                return False
        