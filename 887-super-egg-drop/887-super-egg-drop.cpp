class Solution {
public:
    int superEggDrop(int k, int n) {
        vector<vector<int>> dp(n+1,vector<int>(k+1,0));
        int out=0;
        while(dp[out][k]<n)
        {
            out++;
            for(int i=1;i<k+1;i++)
            {
                dp[out][i]+=dp[out-1][i-1]+dp[out-1][i]+1;
            }
        }
        return out;
    }
};