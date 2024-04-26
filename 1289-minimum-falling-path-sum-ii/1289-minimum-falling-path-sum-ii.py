class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        out=float('inf')
        n=len(mat)
        m=len(mat[0])
        if n==1:
            return min(mat[0])
        if m==1:
            return sum([i[0]for i in mat])
        p1,p2=sorted(mat[0])[:2]
        for r in range(1,n):
            for c in range(m):
                if mat[r-1][c]==p1:
                    mat[r][c]+=p2
                else:
                    mat[r][c]+=p1
            p1,p2=sorted(mat[r])[:2]
        return p1