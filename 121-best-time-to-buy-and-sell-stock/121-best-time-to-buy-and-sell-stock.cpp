class Solution {
public:
    int maxProfit(vector<int>& nums) {
        int cur=-nums[0];
        int out=0;
        for(int i:nums)
        {
            cur=max(cur,-i);
            out=max(out,cur+i);
        }
        return out;
    }
};