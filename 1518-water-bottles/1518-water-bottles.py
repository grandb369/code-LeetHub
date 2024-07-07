class Solution:
    def numWaterBottles(self, n: int, m: int) -> int:
        out=n
        l=0
        while n:
            l+=n
            n=l//m
            l%=m
            out+=n
        return out