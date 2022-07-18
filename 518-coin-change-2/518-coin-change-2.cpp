class Solution {
public:
    int change(int n, vector<int>& coins) {
        if (n==0)return 1;
        vector<int>dp(n+1,0);
        for(int i:coins)
        {
            if(i<=n)dp[i]+=1;
            for(int j=i+1;j<=n;j++)
            {
                dp[j]+=dp[j-i];
            }
        }
        return dp[n];
    }
};