class Solution(object):
    def checkOverlap(self, radius, xc, yc, x1, y1, x2, y2):
        x = max(x1, min(xc, x2)) - xc
        y = max(y1, min(yc, y2)) - yc
        return (x*x + y*y <= radius*radius)
    

        