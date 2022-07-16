class Solution {
public:
    bool isMatch(string s, string p) {
        int n=s.size();
        int m=p.size();
        vector<vector<bool>>dp(n+1,vector<bool>(m+1,false));
        dp[0][0]=true;
        int r,c;
        for(c=1;c<m+1;c++)
        {
            if(p[c-1]=='*')dp[0][c]=dp[0][c-1];
        }
        for(r=1;r<n+1;r++)
        {
            for(c=1;c<m+1;c++)
            {
                if(p[c-1]=='?' || p[c-1]==s[r-1])
                {
                    dp[r][c]=dp[r-1][c-1];
                }
                else if(p[c-1]=='*')
                {
                    dp[r][c]=dp[r-1][c] || dp[r][c-1] || dp[r-1][c-1];
                }
            }
        }
        return dp[n][m];
    }
};