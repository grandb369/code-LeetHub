class Solution:
    def spiralMatrixIII(self, n: int, m: int, r: int, c: int) -> List[List[int]]:
        temp=[(i,j) for j in range(m) for i in range(n)]
        temp.remove((r,c))
        ct=0
        mv=1
        way=[(0,1),(1,0),(0,-1),(-1,0)]
        di=0
        out=[(r,c)]
        while temp:
            x,y=way[di]
            di=(di+1)%4
            for _ in range(mv):
                r+=x
                c+=y
                if (r,c) in temp:
                    temp.remove((r,c))
                    out.append((r,c))
            if ct==1:
                ct=-1
                mv+=1
            ct+=1    
        return out