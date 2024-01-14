class Solution:
    def minSteps(self, s: str, t: str) -> int:
        k=collections.defaultdict(int)
        for i in s:
            k[i]+=1
        out=0
        for i in t:
            if k[i]==0:
                out+=1
            else:
                k[i]-=1
        return out