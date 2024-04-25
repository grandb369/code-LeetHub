class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp=[0 for i in range(26)]
        a=ord('a')
        out=1
        for i in s:
            v=ord(i)
            cur=dp[v-a]
            for j in range(v-k,v+k+1):
                if j<97 or j>122:continue
                key=j-a
                cur=max(dp[key]+1,cur)
                out=max(out,cur)
            dp[v-a]=cur
        return out