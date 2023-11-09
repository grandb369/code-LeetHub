class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x1=min(sx,fx)
        x2=max(sx,fx)
        y1=min(sy,fy)
        y2=max(sy,fy)
        d1=x2-x1
        d2=y2-y1
        if d1==d2==0 and t==1:
            return False
        return t>=max(d1,d2)