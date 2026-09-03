class Solution(object):
    def minWindow(self, s, t):
        need = {}
        avail = {}
        left = 0
        right = 0
        formed = 0
        start = 0
        min_len = float("inf")
        for i in t:
            need[i] = need.get(i, 0) +1
        while right < len(s):
            avail[s[right]] = avail.get(s[right], 0) +1
            if s[right] in need and avail[s[right]] == need[s[right]]:
                formed +=1
            while formed == len(need):
                if right-left + 1 < min_len:
                    min_len = min(min_len, right - left +1)
                    start = left
                avail[s[left]] -=1
                if s[left] in need and avail[s[left]] < need[s[left]]:
                    formed -=1
                left +=1
            right +=1
        if min_len == float("inf"):
            return ""
        return s[start: min_len + start]





        
        