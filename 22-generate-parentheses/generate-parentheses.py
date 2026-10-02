class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        def backtrack(par, open, close):
            if len(par) == n*2:
                ans.append(par)
                return
            if open < n:
                backtrack(par + "(", open +1, close)
            if close < open:
                backtrack(par + ")", open, close +1)
        backtrack("", 0, 0)
        return ans

        
        