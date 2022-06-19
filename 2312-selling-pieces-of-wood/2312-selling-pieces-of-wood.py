class Solution:
    def sellingWood(self, m: int, n: int, pr: List[List[int]]) -> int:
        dp=[[0for i in range(n+1)]for j in range(m+1)]
        for r,c,p in pr:
            dp[r][c]=p
        for i in range(1,m+1):
            for j in range(1,n+1):
                for r in range(1,i//2+1):
                    dp[i][j]=max(dp[i][j],dp[r][j]+dp[i-r][j])
                for c in range(1,j//2+1):
                    dp[i][j]=max(dp[i][j],dp[i][c]+dp[i][j-c])
        return dp[-1][-1]
                    