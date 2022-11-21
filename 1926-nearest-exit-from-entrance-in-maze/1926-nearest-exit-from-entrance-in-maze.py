class Solution:
    def nearestExit(self, mat: List[List[str]], ent: List[int]) -> int:
        temp=set([])
        n=len(mat)
        m=len(mat[0])
        for i in range(m):
            if mat[0][i]=='.' and [0,i]!=ent:
                temp.add((0,i))
            if mat[n-1][i]=='.' and [n-1,i]!=ent:
                temp.add((n-1,i))
        for i in range(n):
            if mat[i][0]=='.' and [i,0]!=ent:
                temp.add((i,0))
            if mat[i][m-1]=='.' and [i,m-1]!=ent:
                temp.add((i,m-1))
        if len(temp)==0:
            return -1
        out=0
        stack=set([(ent[0],ent[1])])
        seen=set([])
        while stack:
            nex=set([])
            for x,y in stack:
                if (x,y)in temp:
                    return out
                for i,j in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny=x+i,y+j
                    if 0<=nx<n and 0<=ny<m and mat[nx][ny]=='.' and (nx,ny)not in seen:
                        seen.add((nx,ny))
                        nex.add((nx,ny))
            out+=1
            stack=nex
        return -1