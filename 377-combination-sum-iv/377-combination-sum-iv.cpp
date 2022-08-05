class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<long>dp(target+1,0);
        sort(nums.begin(),nums.end());
        int mod=2147483647;
        for(int i:nums)
        {
            if(i>target)break;
            dp[i]=1;
        }
        for(int i=0;i<target+1;i++)
        {
            for(int j:nums)
            {
                if(i-j<0)break;
                dp[i]+=dp[i-j];
                dp[i]%=mod;
            }
        }
        return dp.back();
    }
};