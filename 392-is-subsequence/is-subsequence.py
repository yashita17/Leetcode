class Solution(object):
    def isSubsequence(self, s, t):
        m = len(s)
        n = len(t)
        if m > n:
            return False
        j = 0
        i = 0
        while j < m and i < n:
            if t[i] == s[j]:
                i+=1
                j+=1
            else:
                i+=1
        if j == m:
            return True
        return False

        