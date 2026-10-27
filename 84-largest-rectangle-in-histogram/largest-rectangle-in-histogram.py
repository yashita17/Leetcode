class Solution(object):
    def largestRectangleArea(self, he):
        stack = []
        maxArea = 0
        for i in range(len(he)):
            while stack and he[i]< he[stack[-1]]:
                h = he[stack.pop()]
                if stack:
                    w = i - stack[-1] -1
                else:
                    w = i
                maxArea = max(maxArea, w*h)
            stack.append(i)
        while stack:
            h = he[stack.pop()]
            if stack:
                w = len(he) - stack[-1] -1
            else:
                w = len(he)
            maxArea = max(maxArea, h*w)
        
        return maxArea
        
        