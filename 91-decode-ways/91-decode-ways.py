class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        dp=[0 for i in range(len(s))]
        dp[0]=1
        for i in range(1,len(s)):
            cur=0
            val=int(s[i])
            if val>0 and val<10:
                cur+=dp[i-1]
            val=int(s[i-1]+s[i])
            if val>0 and val<27 and s[i-1]!='0':
                if i>1:
                    cur+=dp[i-2]
                else:
                    cur+=1
            dp[i]=cur
        return dp[-1]