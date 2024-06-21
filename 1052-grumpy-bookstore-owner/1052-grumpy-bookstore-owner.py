class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        n=len(c)
        val=sum([c[i]for i in range(n) if not g[i]])
        cur=sum([c[i]for i in range(m) if g[i]])
        out=val+cur
        for i in range(m,n):
            if g[i]:
                cur+=c[i]
            if g[i-m]:
                cur-=c[i-m]
            out=max(out,val+cur)
        return out