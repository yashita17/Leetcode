class Solution(object):
    def largestOverlap(self, img1, img2):
        a = []
        b = []
        
        n = len(img1)
        
        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    a.append((i, j))
                if img2[i][j] == 1:
                    b.append((i, j))
        
        d = {}
        ans = 0
        
        for x1, y1 in a:
            for x2, y2 in b:
                shift = (x2 - x1, y2 - y1)
                d[shift] = d.get(shift, 0) + 1
                ans = max(ans, d[shift])
        
        return ans