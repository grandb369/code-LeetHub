class Solution:
    def checkStraightLine(self, c: List[List[int]]) -> bool:
        c.sort()
        y=c[1][1]-c[0][1]
        x=c[1][0]-c[0][0]
        b=c[0][1]*x-c[0][0]*y
        for i in range(2,len(c)):
            if c[i][1]*x!=(c[i][0]*y+b):
                return False
        return True