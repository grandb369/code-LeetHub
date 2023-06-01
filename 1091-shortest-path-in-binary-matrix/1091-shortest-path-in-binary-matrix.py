class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1or grid[-1][-1]==1:
            return -1
        di=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        n=len(grid)
        stack=[(0,0)]
        grid[0][0]=1
        out=1
        while stack:
            temp=[]
            for i,j in stack:
                if i==j==n-1:
                    return out
                for ii,jj in di:
                    x=i+ii
                    y=j+jj
                    if 0<=x<n and 0<=y<n and grid[x][y]==0:
                        grid[x][y]=1
                        temp.append((x,y))
            out+=1
            stack=temp
        return -1