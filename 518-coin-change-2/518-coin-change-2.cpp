class Solution {
public:
    int change(int n, vector<int>& nums) {
        if(n==0)return 1;
        vector<int>dp(n+1,0);
        for(int c:nums)
        {
            if(c>n)continue;
            dp[c]++;
            for(int i=c;i<=n;i++)
            {
                dp[i]+=dp[i-c];
            }
        }
        return dp[n];
    }
};