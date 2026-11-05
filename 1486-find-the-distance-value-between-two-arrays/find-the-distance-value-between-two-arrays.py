class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count = 0
        for i in arr1:
            flag = True
            for j in arr2:
                if abs(i-j) <=d:
                    flag = False
            if flag:
                count +=1
        return count
                
        