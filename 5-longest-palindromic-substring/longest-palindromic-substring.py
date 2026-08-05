class Solution(object):
    def longestPalindrome(self, s):
        ans = ""
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -=1
                right +=1
            return s[left+1 : right]
        for i in range (len(s)):
            str1 = expand(i,i)
            str2 = expand(i, i+1)
            if len(ans) < len(str1):
                ans = str1
            if len(ans) < len(str2):
                ans = str2
        return ans
                    

        
        