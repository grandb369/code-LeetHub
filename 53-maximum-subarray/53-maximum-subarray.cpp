class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int out=nums[0];
        int cur=nums[0];
        for(int i=1;i<nums.size();i++)
        {
            cur=max(cur+nums[i],nums[i]);
            out=max(out,cur);
        }
        return out;
    }
};