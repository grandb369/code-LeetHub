class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        out=0
        points.sort()
        s=e=float('-inf')
        for i,j in points:
            if i>e:
                out+=1
                s,e=i,j
            else:
                e=min(e,j)
        return out