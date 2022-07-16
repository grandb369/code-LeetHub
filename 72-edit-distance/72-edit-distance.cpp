class Solution {
public:
    int minDistance(string w1, string w2) {
        int n=w1.size();
        int m=w2.size();
        vector<vector<int>>dp(n+1,vector<int>(m+1,0));
        int r,c;
        for(r=0;r<n+1;r++)dp[r][0]=r;
        for(c=0;c<m+1;c++)dp[0][c]=c;
        for(r=1;r<n+1;r++)
        {
            for(c=1;c<m+1;c++)
            {
                if(w1[r-1]==w2[c-1])dp[r][c]=dp[r-1][c-1];
                else dp[r][c]=min(dp[r-1][c-1],min(dp[r-1][c],dp[r][c-1]))+1;
            }
        }
        return dp[n][m];
    }
};