class Solution {
public:
    int numberOfSubarrays(vector<int>& nums, int k) {
        long out=0;
        vector<int>dp;
        long count=0;
        long n=nums.size();
        for(int i=0;i<n;i++)
        {
            if(nums[i]%2==0)count++;
            else
            {
                dp.push_back(count);
                count=0;
            }
        }
        dp.push_back(count);
        int m=dp.size();
        for(int i=0;i<max(0,m-k);i++)
        {
            int l=dp[i]+1;
            int r=dp[i+k]+1;
            out+=l*r;
        }
        return out;
    }
};