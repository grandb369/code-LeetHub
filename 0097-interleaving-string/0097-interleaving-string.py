class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2==s3
        if not s2:
            return s1==s3
        if len(s1)+len(s2)!=len(s3):
            return False
        s1=' '+s1
        n1=len(s1)
        s2=' '+s2
        n2=len(s2)
        s3=' '+s3
        dp=[False for i in range(n2)]
        for r in range(n1):
            for c in range(n2):
                if r==0 and c==0:
                    dp[r]=True
                elif c==0:
                    dp[c]=dp[c]and s1[r]==s3[r]
                elif r==0:
                    dp[c]=dp[c-1]and s2[c]==s3[r+c]
                else:
                    dp[c]=(dp[c-1]and s2[c]==s3[r+c])or(dp[c]and s1[r]==s3[r+c])
        return dp[-1]