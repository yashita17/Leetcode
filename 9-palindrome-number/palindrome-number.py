class Solution(object):
    def isPalindrome(self, x):
        x1 = x
        s = 0
        while(x>0):
            r = x%10
            s = s*10 + r    
            x = x/10
        if x1 == s:
             return True
        else:
            return False
n = Solution()
print(n.isPalindrome(121))