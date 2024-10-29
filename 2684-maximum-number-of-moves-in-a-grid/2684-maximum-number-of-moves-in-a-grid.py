class Solution:
    def maxMoves(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        dp=[[0 for i in range(m)]for i in range(n)]
        out=0
        for c in range(1,m):
            for r in range(n):
                if r>0 and mat[r-1][c-1]<mat[r][c] and (c-1==0 or dp[r-1][c-1]!=0):
                    dp[r][c]=max(dp[r][c],dp[r-1][c-1]+1)
                if mat[r][c-1]<mat[r][c] and (c-1==0 or dp[r][c-1]!=0):
                    dp[r][c]=max(dp[r][c],dp[r][c-1]+1)
                if r<n-1 and mat[r+1][c-1]<mat[r][c] and (c-1==0 or dp[r+1][c-1]!=0):
                    dp[r][c]=max(dp[r][c],dp[r+1][c-1]+1)
                out=max(out,dp[r][c])
        return out