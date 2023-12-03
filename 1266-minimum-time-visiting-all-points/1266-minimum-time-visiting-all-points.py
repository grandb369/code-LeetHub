class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        out=0
        x,y=points.pop(0)
        for i,j in points:
            out+=max(abs(x-i),abs(y-j))
            x,y=i,j
        return out