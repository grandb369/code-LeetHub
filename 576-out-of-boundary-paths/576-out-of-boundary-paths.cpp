class Solution {
public:
    int cal(int m, int n, int r, int c, int val, vector<vector<int>>& dp2)
    {
        int mod=1000000007;
        if(0<=r && r<m && 0<=c && c<n)
        {
            
            dp2[r][c]+=val;
            dp2[r][c]%=mod;
            return 0;
        }
        else
        {
            return val;
        }
    }
    int findPaths(int m, int n, int t, int sr, int sc) {
        int out=0;
        vector<vector<int>>dp(m,vector<int>(n,0));
        vector<vector<int>>dp2(m,vector<int>(n,0));
        int mod=1e9+7;
        dp[sr][sc]=1;
        int i,r,c;
        for(i=0;i<t;i++)
        {
            for(r=0;r<m;r++)
            {
                for(c=0;c<n;c++)
                {
                    out+=cal(m,n,r-1,c,dp[r][c],dp2);
                    out%=mod;
                    out+=cal(m,n,r+1,c,dp[r][c],dp2);
                    out%=mod;
                    out+=cal(m,n,r,c-1,dp[r][c],dp2);
                    out%=mod;
                    out+=cal(m,n,r,c+1,dp[r][c],dp2);
                    out%=mod;
                }
            }
            dp=dp2;
            for(r=0;r<m;r++)
            {
                for(c=0;c<n;c++)
                {
                    dp2[r][c]=0;
                }
            }
        }
        return out;
    }
};