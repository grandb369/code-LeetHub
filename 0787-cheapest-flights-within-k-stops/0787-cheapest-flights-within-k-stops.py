class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        out=[float('inf') for i in range(n)]
        g=collections.defaultdict(set)
        for u,v,c in flights:
            g[u].add((v,c))
        stack=[src]
        out[src]=0
        for i in range(k+1):
            temp=set()
            ans=out[:]
            for cur in stack:
                for nex,c in g[cur]:
                    temp.add(nex)
                    ans[nex]=min(ans[nex],out[cur]+c)
            stack=temp
            out=ans
        if out[dst]==float('inf'):
            return -1
        return out[dst]