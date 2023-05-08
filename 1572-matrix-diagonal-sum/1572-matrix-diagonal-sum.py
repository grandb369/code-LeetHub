class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        out=0
        n=len(mat)-1
        for r in range(len(mat)):
            seen=set([])
            if (r,r)not in seen:
                out+=mat[r][r]
            seen.add((r,r))
            if (r,n-r)not in seen:
                out+=mat[r][n-r]
        return out