class Solution(object):
    def checkDivisibility(self, n):
        s = 0
        p = 1
        n1 = n
        n2 = n
        while n1 !=0:
            r = n1 % 10
            s +=r
            n1 = n1//10
        while n2 !=0:
            r = n2 % 10
            p *=r
            n2 = n2//10
        if  n % (s+p) == 0:
            return True
        return False
        
        