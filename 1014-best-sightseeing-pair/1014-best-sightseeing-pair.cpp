class Solution {
public:
    int maxScoreSightseeingPair(vector<int>& nums) {
        int pre=nums[0];
        int out=0;
        for(int i=1;i<nums.size();i++)
        {
            pre--;
            out=max(out,nums[i]+pre);
            pre=max(pre,nums[i]);
        }
        return out;
    }
};