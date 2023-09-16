from heapq import *
class Solution:
    def minimumEffortPath(self, h: List[List[int]]) -> int:
        n=len(h)
        m=len(h[0])
        seen=[[False for i in range(m)]for i in range(n)]
        ans=[[inf for i in range(m)]for i in range(n)]
        stack=[(0,0,0)]
        ans[0][0]=0
        while stack:
            v,r,c=heappop(stack)
            if r==n-1 and c==m-1:
                return ans[r][c]
            if v>ans[r][c]:
                continue
            seen[r][c]=True
            for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                nr,nc=r+i,c+j
                if 0<=nr<n and 0<=nc<m and not seen[nr][nc]:
                    val=abs(h[nr][nc]-h[r][c])
                    val=max(val,ans[r][c])
                    if ans[nr][nc]>val:
                        ans[nr][nc]=val
                        heappush(stack,(ans[nr][nc],nr,nc))
                        