class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        if k==0:
            return 1
        mod=10**9+7
        dp=[1]
        nn=1
        c=0
        for i in range(1,n+1):
            nex=[]
            nn+=i
            nn=min(nn,k+1)
            for j in range(nn):
                val=0
                if j!=0:
                    val=nex[-1]
                if j<len(dp):
                    val+=dp[j]
                if j-i>=0 and j-i<len(dp):
                    val-=dp[j-i]
                nex.append(val%mod)
                c+=1
            dp=nex
        if k>=len(dp):
            return 0
        return dp[k]%mod