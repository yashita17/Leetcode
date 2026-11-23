class Solution(object):
    def wordBreak(self, s, wordDict):
        words = set(wordDict)
        n = len(s)
        dp = [-1]*n
        def solve(i):
            if i == n:
                return True 
            
            if dp[i] != -1:
                return dp[i]
            for j in range(i,n):
                word = s[i:j+1]
                if word in words and solve(j+1):
                    dp[i] = True
                    return True
            
            dp[i] = False
            return False
        return solve(0)
        