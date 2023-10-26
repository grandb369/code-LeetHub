class Solution {
public:
    int numFactoredBinaryTrees(vector<int>& nums) {
        int out=0;
        int n=nums.size();
        sort(nums.begin(),nums.end());
        int mod=1000000007;
        unordered_map<long,long>dp;
        set<int>temp;
        for(auto i:nums)
        {
            dp[i]=1;
            temp.insert(i);
        }
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                if(nums[i]%nums[j]==0 && temp.count((int)nums[i]/nums[j]))
                {
                    dp[nums[i]]+=dp[nums[j]]*dp[(int)nums[i]/nums[j]];
                    dp[nums[i]]%=mod;
                }
            }
        }
        for(auto i:nums)
        {
            out+=dp[i];
            out%=mod;
        }
        return out;
    }
};