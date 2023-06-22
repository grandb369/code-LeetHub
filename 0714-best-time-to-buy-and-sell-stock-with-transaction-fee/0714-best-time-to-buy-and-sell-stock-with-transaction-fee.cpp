class Solution {
public:
    int maxProfit(vector<int>& nums, int fee) {
        int buy=-nums[0];
        int sell=0;
        for(int i:nums)
        {
            int temp=sell;
            sell=max(sell,i+buy-fee);
            buy=max(temp-i,buy);
        }
        return sell;
    }
};