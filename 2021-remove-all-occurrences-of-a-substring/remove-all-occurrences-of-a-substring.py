class Solution(object):
    def removeOccurrences(self, s, part):
        while(s.find(part)!=-1):
            s = s[:s.find(part)] + s[s.find(part) + len(part):]

        return s
        
        