class Solution {
public:
    int maxProfit(vector<int>& nums) {
        int out=0;
        int cur=nums[0];
        for(int i:nums)
        {
            out=max(out,i-cur);
            cur=min(cur,i);
        }
        return out;
    }
};