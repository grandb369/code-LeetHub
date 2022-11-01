class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)
        m=len(grid[0])
        if m==1:
            return [-1]
        out=[]
        for i in range(m):
            c=i
            ans=-1
            for r in range(n):
                if grid[r][c]==1:
                    if c+1<m and grid[r][c+1]==-1:
                        ans=-1
                        break
                    c+=1
                else:
                    if c-1>=0 and grid[r][c-1]==1:
                        ans=-1
                        break
                    c-=1
                if c<0 or c>=m:
                    ans=-1
                    break
                ans=c
            out.append(ans)
        return out