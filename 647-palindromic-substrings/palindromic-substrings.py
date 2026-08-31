class Solution(object):
    def expand(self,s,i,j):
        count = 0
        while(i>=0 and j< len(s) and s[i]==s[j]):
            count +=1
            i-=1
            j+=1
        return count
    def countSubstrings(self, s):
        total_count = 0
        for i in range(len(s)):
            j = i
            oddAns = self.expand(s,i,j)
            j = i+1
            evenAns = self.expand(s,i,j)
            total_count += oddAns + evenAns
        return total_count
    



                                                                    
        