class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        def check(r,c):
            return 0<=r<len(M)and 0<=c<len(M[0])
        def add(r,c):
            out=0
            base=0
            for i,j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1),(0,0)]:
                if check(r+i,c+j):
                    out+=M[r+i][c+j]
                    base+=1
            return out//base
        out=[[0 for i in range(len(M[0]))]for i in range(len(M))]
        for r in range(len(M)):
            for c in range(len(M[0])):
                out[r][c]=add(r,c)
        return out