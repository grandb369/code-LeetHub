class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph=collections.defaultdict(list)
        pro=dict()
        for i,(u,v)in enumerate(edges):
            graph[u].append(v)
            graph[v].append(u)
            pro[u,v]=pro[v,u]=succProb[i]
        out=0
        seen=set([])
        stack=[(-1,start)]
        while stack:
            c,u=heappop(stack)
            if u==end:
                return -c
            seen.add(u)
            for v in graph[u]:
                if v not in seen:
                    p=c*pro.get((u,v),0)
                    heappush(stack,(p,v))
        return out
                        