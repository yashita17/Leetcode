class Solution(object):
    def validPalindrome(self, s):
        def isPalindrome(s, left, right):
            while left < right:
                if s[left] == s[right]:
                    left +=1
                    right -=1
                else:
                    return False
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(s, left +1, right) or isPalindrome(s, left, right-1)
            else:
                left +=1
                right -=1
        return True

        
        