class Solution:
    def maxValue(self, n: int, index: int, ms: int) -> int:
        if index==0 or index==n-1:
            if ms<=n:
                return 1
            if n==1:
                return ms
            ms=ms-n-1
            out=2
            nex=2
            while ms-nex>=0:
                ms-=nex
                out+=1
                if nex<n:
                    nex+=1
                else:
                    out+=ms//n
                    return out
            return out
        else:
            if ms<=n:
                return 1
            ms=ms-n-1
            out=2
            l=index-1
            r=index+1
            while l>0 or r<n-1:
                ran=r-l+1
                if ran>ms:
                    return out
                ms-=ran
                out+=1
                if r<n-1:
                    r+=1
                if l>0:
                    l-=1
            if ms>=n:
                out+=(ms//n)
            return out