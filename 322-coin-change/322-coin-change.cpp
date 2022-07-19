class Solution {
public:
    int coinChange(vector<int>& coins, int n) {
        if (n==0)return 0;
        vector<int>dp(n+1,-1);
        sort(coins.begin(),coins.end());
        while(coins.size()>0 && coins.back()>n)
        {
            coins.pop_back();
        }
        for(int i:coins)dp[i]=1;
        for(int i=1;i<=n;i++)
        {
            if (dp[i]==-1)continue;
            for(int j:coins)
            {
                if(i+j>n)break;
                if(dp[i+j]==-1)dp[i+j]=dp[i]+1;
                else dp[i+j]=min(dp[i+j],dp[i]+1);
            }
        }
        return dp[n];
    }
};