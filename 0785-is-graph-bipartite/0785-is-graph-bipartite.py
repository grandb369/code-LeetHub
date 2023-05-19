class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        k={0:set([]),1:set([])}
        stack=[0]
        seen=set([0])
        c=0
        left=set([i for i in range(len(graph))])
        while stack:
            temp=set([])
            for i in stack:
                seen.add(i)
                if i in left:
                    left.remove(i)
                if i in k[1-c]:
                    return False
                k[c].add(i)
                for j in graph[i]:
                    if j not in seen:
                        temp.add(j)
            stack=temp
            c=1-c
            if not stack and left:
                stack.add(left.pop())
        return True