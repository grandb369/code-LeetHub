class Solution {
public:
    bool carPooling(vector<vector<int>>& nums, int c) {
        int ma=0;
        int n=nums.size();
        for (int i=0;i<n;i++)
        {
            ma=max(ma,nums[i][2]);
        }
        vector<int>dp(ma+1,0);
        for(int i=0;i<n;i++)
        {
            dp[nums[i][1]]+=nums[i][0];
            dp[nums[i][2]]-=nums[i][0];
        }
        int val=0;
        for(int i=0;i<ma+1;i++)
        {
            val+=dp[i];
            if(val>c)return false;
        }
        return true;
    }
};