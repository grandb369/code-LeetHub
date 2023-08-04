class Solution:
    def wordBreak(self, s: str, w: List[str]) -> bool:
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        for i in range(len(s)):
            for j in w:
                if j==s[i-len(j)+1:i+1] and dp[i-len(j)+1]:
                    dp[i+1]=True
        return dp[-1]