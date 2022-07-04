class Solution {
public:
    int candy(vector<int>& nums) {
        int n=nums.size();
        vector<int>dp(n,1);
        for (int i=1;i<n;i++)
        {
            if(nums[i]>nums[i-1] && dp[i]<=dp[i-1])
            {
                dp[i]=dp[i-1]+1;
            }
        }
        for(int i=n-2;i>=0;i--)
        {
            if(nums[i]>nums[i+1] && dp[i]<=dp[i+1])
            {
                dp[i]=dp[i+1]+1;
            }
        }
        int out=0;
        for (int i:dp)
        {
            out+=i;
        }
        return out;
    }
};