class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        k=collections.defaultdict(set)
        for u,v in roads:
            k[u].add(v)
            k[v].add(u)
        if not n or not roads:
            return 0
        key=sorted(k.keys(),key=lambda x:len(k[x]))
        out=0
        for i in range(len(key)):
            l=len(k[key[i]])
            for j in k[key[i]]:
                k[j].remove(key[i])
            r=0
            for j in range(i+1,len(key)):
                r=max(r,len(k[key[j]]))
            for j in k[key[i]]:
                k[j].add(key[i])
            out=max(out,l+r)
        return out