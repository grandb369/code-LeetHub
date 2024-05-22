class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False for i in range(n)]for i in range(n)]
        for i in range(n):
            dp[i][i]=True
        for i in range(n):
            l=i-1
            r=i+1
            while l>=0 and r<n and s[l]==s[r]:
                dp[l][r]=True
                l-=1
                r+=1
        for i in range(1,n):
            if s[i-1]==s[i]:
                dp[i-1][i]=True
                l=i-2
                r=i+1
                while l>=0 and r<n and s[l]==s[r]:
                    dp[l][r]=True
                    l-=1
                    r+=1
        self.out=[]
        def back(cur,temp):
            if cur==n-1:
                self.out.append(temp)
            else:
                for i in range(cur+1,n):
                    if dp[cur+1][i]:
                        back(i,temp+[s[cur+1:i+1]])
        back(-1,[])
        return self.out