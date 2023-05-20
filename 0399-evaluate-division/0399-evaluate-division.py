class Solution:
    def calcEquation(self, e: List[List[str]], v: List[float], q: List[List[str]]) -> List[float]:
        
        for i in range(len(e)):
            e[i].append(v[i])
        graph=collections.defaultdict(list)
        for u,v,t in e:
            graph[u].append([v,t])
            graph[v].append([u,1/t])
        def search(i,j,graph,pre,visited):
            if j==i:
                return pre
            if i not in graph.keys():
                return -1
            temp=-1
            for new,val in graph[i]:
                if new not in visited:
                    visited.append(new)
                    temp=search(new,j,graph,pre*val,visited)
                    if temp!=-1:
                        return temp
            return temp
        out=[]
        for i,j in q:
            visited=[i]
            if i not in graph.keys():
                out.append(float(-1))
            else:
                out.append(search(i,j,graph,1,visited))
        return out