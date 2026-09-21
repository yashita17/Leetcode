class Solution(object):
    def canCross(self, stones):
        stone_set = set(stones)
        n = len(stones)
        dp = {}
        def solve(pos, k):
            if pos == stones[-1]:
                return True
            if (pos,k) in dp: 
                return dp[(pos,k)]
            for jumps in [k-1, k, k+1]:
                if jumps <= 0:
                    continue
                next_pos = pos + jumps
                if next_pos in stone_set:
                    if solve(next_pos, jumps):
                        dp[(pos,k)] = True
                        return True
            dp[(pos,k)] = False
            return False
        return solve(0,0)
            
        