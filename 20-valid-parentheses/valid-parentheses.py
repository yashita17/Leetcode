class Solution(object):
    def isValid(self, s):
        bracket = {')' : '(', '}': '{', ']': '['}
        stack = []
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if bracket[i] != stack[-1]:
                    return False

                stack.pop()
        return not stack





        
        