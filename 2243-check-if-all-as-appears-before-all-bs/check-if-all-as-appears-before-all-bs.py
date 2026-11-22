class Solution(object):
    def checkString(self, s):
        i = 0
        while i < len(s) and s[i] != 'b':
            i +=1
        for c in range(i,len(s)):
            if s[c] == 'a':
                return False
            
        return True


        