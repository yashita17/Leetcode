class Solution(object):
    def maximumLengthSubstring(self, s):
        dict = {}
        l = 0
        max_l = 1
        for i in range(len(s)):
            dict[s[i]] = dict.get(s[i], 0) +1
            while dict[s[i]] > 2:
                dict[s[l]] -= 1
                l += 1
            length = (i-l) + 1
            max_l = max(length, max_l)
        return max_l
                


        
        