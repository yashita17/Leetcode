class Solution(object):
    def canAliceWin(self, n):
        turn = 0
        stones = 10
        while n >= stones:
            n -= stones
            stones-=1
            turn +=1
        return turn % 2== 1
        