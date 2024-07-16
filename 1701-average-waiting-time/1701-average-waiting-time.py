class Solution:
    def averageWaitingTime(self, c: List[List[int]]) -> float:
        n=len(c)
        s,e=c.pop(0)
        out=e
        e+=s
        for i,j in c:
            if e<=i:
                s,e=i,i+j
                out+=j
            else:
                e+=j
                out+=(e-i)
                s=i
        return out/n