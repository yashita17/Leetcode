class Solution(object):
    def maxDepth(self, s):
        count = 0
        max_depth = 0
        for i in s:
            if i == "(":
                count +=1
                max_depth = max(count, max_depth)
            elif i == ")":
                count -=1
            else:
                continue
        return max_depth




        