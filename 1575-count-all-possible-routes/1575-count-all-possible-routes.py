class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        mod=10**9+7
        n=len(locations)
        dp=[[0 for i in range(n)]for i in range(fuel+1)]
        dp[0][start]=1
        for f in range(fuel):
            for i in range(n):
                for j in range(n):
                    if i==j or f+abs(locations[i]-locations[j])>fuel:
                        continue
                    dp[f+abs(locations[i]-locations[j])][j]=(dp[f+abs(locations[i]-locations[j])][j]+dp[f][i])%mod
        out=0
        for i in range(fuel+1):
            out=(out+dp[i][finish])%mod
        return out