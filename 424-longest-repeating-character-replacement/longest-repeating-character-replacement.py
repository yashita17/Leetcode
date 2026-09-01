class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        right = 0
        max_len = 0
        freq = {}
        while right < len(s):
            freq[s[right]] = freq.get(s[right],0) +1
            val_tuple = freq.values()
            maxFreq = max(val_tuple)
            while (right - left + 1) - maxFreq > k:
                freq[s[left]] -=1
                left +=1
            length = right - left +1
            max_len = max(length, max_len)
            right +=1
        return max_len
        
        