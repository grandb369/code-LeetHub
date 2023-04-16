class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n=len(target)
        m=len(words[0])
        mod=10**9+7
        if n>m:
            return 0
        temp=[collections.defaultdict(int) for i in range(m)]
        diff=m-n+1
        for i in words:
            for j in range(m):
                temp[j][i[j]]+=1
        dp=[temp[i][target[0]]for i in range(diff)]
        for i in range(1,n):
            nex=[]
            su=0
            for j in range(diff):
                su+=dp[j]
                nex.append(temp[i+j][target[i]]*su%mod)
            dp=nex
        return sum(dp)%mod