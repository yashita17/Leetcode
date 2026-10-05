class Solution(object):
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key = lambda x:(x[0], -x[1]))
        height = []
        for e in envelopes:
            height.append(e[1])
        tail =[]
        for n in height:
            pos = self.celing(tail, n)
            if pos == len(tail):
                tail.append(n)
            else:
                tail[pos] = n
        return len(tail)
    def celing(self, tail, target):
        low = 0
        high = len(tail)
        while low < high:
            mid = (low + high)//2
            if tail[mid]< target:
                low = mid +1
            else:
                high = mid
        return low