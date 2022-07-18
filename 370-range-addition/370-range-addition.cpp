class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int>dp(length,0);
        for(vector<int> cur:updates)
        {
            dp[cur[0]]+=cur[2];
            if(cur[1]+1<length)dp[cur[1]+1]-=cur[2];
        }
        int val=0;
        for(int i=0;i<length;i++)
        {
            dp[i]+=val;
            val=dp[i];
        }
        return dp;
    }
};