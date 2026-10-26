class Solution(object):
    def countIslands(self, grid, k):
        m = len(grid)
        n = len(grid[0])
        ans = 0
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]== 0:
                return 0
            total = grid[r][c]
            grid[r][c] = 0
            total += dfs(r+1, c)
            total += dfs(r-1, c)
            total += dfs(r, c+1)
            total += dfs(r, c-1)
            return total
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] >0:
                    total = dfs(i, j)
                    if total % k == 0:
                        ans +=1
        return ans


        