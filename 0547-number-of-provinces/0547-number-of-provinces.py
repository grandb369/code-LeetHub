class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited=set()
        out=0
        def dfs(i):
            for j in range(len(M[i])):
                if j not in visited and M[i][j]:
                    visited.add(i)
                    dfs(j)
        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                out+=1
        return out