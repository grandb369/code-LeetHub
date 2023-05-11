class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp=[[0 for i in range(len(A))]for i in range(len(B))]
        if A[0]==B[0]:
            dp[0][0]=1
        for i in range(len(A)):
            if A[i]==B[0]:
                dp[0][i]=1
            else:
                dp[0][i]=dp[0][i-1]
        for i in range(len(B)):
            if A[0]==B[i]:
                dp[i][0]=1
            else:
                dp[i][0]=dp[i-1][0]
        for r in range(1,len(B)):
            for c in range(1,len(A)):
                if A[c]==B[r]:
                    dp[r][c]=max(dp[r-1][c-1]+1,dp[r][c-1],dp[r-1][c])
                else:
                    dp[r][c]=max(dp[r-1][c-1],dp[r][c-1],dp[r-1][c])
        return dp[-1][-1]