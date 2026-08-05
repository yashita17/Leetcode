class Solution(object):
    def reverse(self, x):
     
        if(x>=(-2**31)and x<2**31):
            if x< 0:
                sign = -1 
            else:
                sign = 1
            x = abs(x)
            x1 = x
            s = 0
            while(x>0):
                r = x%10
                s = s*10 + r
                x = x//10
            s = s * sign
            if s < -2**31 or s>= 2**31:
                return 0
            return s
        else:
            return 0
        
