class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m=len(rolls)
        su=sum(rolls)
        target=(m+n)*mean
        val=target-su
        if val//n<1 or val//n>6:
            return []
        if val//n==6 and val%n:
            return []
        out=[]
        mod=val%n
        for i in range(n):
            v=val//n
            if mod:
                v+=1
                mod-=1
            out.append(v)
        return out