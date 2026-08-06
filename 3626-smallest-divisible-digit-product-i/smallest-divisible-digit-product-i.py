class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            if n == 0:
                return 0
            
            else:
            
                n1 =  n
                multi = 1
                while(n1 !=0):
                    r= n1%10
                    multi = multi * r
                    n1 = n1//10
                if multi % t == 0:
                    return n
            n+=1
        