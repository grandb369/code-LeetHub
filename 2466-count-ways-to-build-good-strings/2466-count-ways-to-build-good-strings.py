class Solution:
    def countGoodStrings(self, low: int, high: int, z: int, o: int) -> int:
        dp=[0 for i in range(high+1)]
        dp[0]=1
        for i in range(1,high+1):
            if i-z>=0:
                dp[i]+=dp[i-z]
            if i-o>=0:
                dp[i]+=dp[i-o]
        mod=10**9+7
        out=0
        for i in range(low,high+1):
            out+=dp[i]
        return out%mod