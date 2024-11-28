class Solution:
    def minimumObstacles(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        zero=deque([(0,0,0)])
        one=deque([])
        seen=set([])
        while zero or one:
            if zero:
                x,y,c=zero.popleft()
            else:
                x,y,c=one.popleft()
 
            if x==n-1 and y==m-1:
                return c
            for nx,ny in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
                if 0<=nx<n and 0<=ny<m:
                    nex=(nx,ny,c+mat[nx][ny])
                    if (nx,ny) not in seen:
                        if mat[nx][ny]:
                            one.append(nex)
                        else:
                            zero.append(nex)
                        seen.add((nx,ny))