class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        out=1
        inc=1
        while time:
            out+=inc
            if out==n or out==1:
                inc*=-1
            time-=1
        return out