class Solution(object):
    def removeDuplicates(self, s):
        stack = []
        for i in range (len(s)):
            if not stack or s[i] != stack[-1]:
                stack.append(s[i])
            else:
                stack.pop()
        return "".join(stack)
        