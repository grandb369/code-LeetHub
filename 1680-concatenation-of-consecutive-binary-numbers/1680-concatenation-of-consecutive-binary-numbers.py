class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod=10**9+7
        out=0
        for i in range(1,n+1):
            val=len(bin(i))-2
            out=out*2**val+i
            out%=mod
        return out