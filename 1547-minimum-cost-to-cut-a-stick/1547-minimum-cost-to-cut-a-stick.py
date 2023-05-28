class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        dp=[[0 for i in range(102)]for i in range(102)]
        cuts=[0]+cuts+[n]
        m=len(cuts)
        for i in range(m-1,-1,-1):
            for j in range(i+1,m):
                if j>i+1:
                    dp[i][j]=float('inf')
                    for k in range(i+1,j+1):
                        dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j])
                dp[i][j]+=cuts[j]-cuts[i]
        return dp[0][len(cuts)-1]-n