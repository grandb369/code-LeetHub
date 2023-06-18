class Solution:
    def countPaths(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        mod=10**9+7
        k=collections.defaultdict(list)
        dp=[[1 for i in range(m)]for i in range(n)]
        for r in range(n):
            for c in range(m):
                k[mat[r][c]].append((r,c))
        for i in sorted(k.keys()):
            for r,c in k[i]:
                for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    x=r+i
                    y=c+j
                    if 0<=x<n and 0<=y<m and mat[x][y]>mat[r][c]:
                        dp[x][y]+=dp[r][c]
        out=0
        #print(k)
        for i in dp:
            #print(i)
            for j in i:
                out+=j
        return out%mod