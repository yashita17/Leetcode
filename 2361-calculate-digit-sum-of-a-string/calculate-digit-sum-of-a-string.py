class Solution(object):
    def digitSum(self, s, k):
        while len(s)>k:
            res = ""

            for i in range(0, len(s), k):
                g = s[i:i+k]
                total = sum(int(x) for x in g)
                res += str(total)
            s = res
        return s
        