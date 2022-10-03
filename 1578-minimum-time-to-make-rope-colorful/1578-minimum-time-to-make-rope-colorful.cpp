class Solution {
public:
    int minCost(string col, vector<int>& nums) {
        int out=0;
        int cur=nums[0];
        char pre=col[0];
        for(int i=1;i<col.size();i++)
        {
            if(pre!=col[i])
            {
                cur=nums[i];
            }
            else
            {
                if (cur>nums[i])
                {
                    out+=nums[i];
                }
                else
                {
                    out+=cur;
                    cur=nums[i];
                }
            }
            pre=col[i];
        }
        return out;
    }
};