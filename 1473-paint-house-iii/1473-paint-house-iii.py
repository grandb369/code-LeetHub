class Solution:
    def minCost(self, nums: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp=[[[float('inf')for i in range(target)]for j in range(n)]for x in range(m)]
        if nums[0]==0:
            for i in range(n):
                dp[0][i][0]=cost[0][i]
        else:
            dp[0][nums[0]-1][0]=0
        #print(dp[0])
        for i in range(1,m):
            if nums[i]==0:
                for t in range(target):
                    for c in range(n):
                        if t==0:
                            dp[i][c][t]=dp[i-1][c][t]+cost[i][c]
                        else:
                            for c2 in range(n):
                                if c!=c2:
                                    dp[i][c][t]=min(dp[i][c][t],dp[i-1][c2][t-1]+cost[i][c])
                                else:
                                    dp[i][c][t]=min(dp[i][c][t],dp[i-1][c][t]+cost[i][c])
            else:
                for t in range(target):
                    c=nums[i]-1
                    if t==0 and nums[i]==c+1:
                        dp[i][c][t]=dp[i-1][c][t]
                    else:
                        for c2 in range(n):
                            if c!=c2:
                                dp[i][c][t]=min(dp[i][c][t],dp[i-1][c2][t-1])
                            else:
                                dp[i][c][t]=min(dp[i][c][t],dp[i-1][c][t])
            #print(dp[i])
        out=float('inf')
        if nums[-1]==0:
            for i in dp[-1]:
                out=min(out,i[-1])
        else:
            out=dp[-1][nums[-1]-1][-1]
        if out==float('inf'):
            return -1
        return out