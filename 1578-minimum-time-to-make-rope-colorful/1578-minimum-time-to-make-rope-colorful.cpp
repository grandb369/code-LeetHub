class Solution {
public:
    int minCost(string col, vector<int>& nums) {
        int out=0;
        int su=nums[0];
        vector<int>stack{nums[0]};
        char pre=col[0];
        for(int i=1;i<col.size();i++)
        {
            su+=nums[i];
            if(pre!=col[i])
            {
                out+=stack[0];
                stack.clear();
            }
            pre=col[i];
            while(stack.size()>0 && stack.back()<nums[i])
            {
                stack.pop_back();
            }
            stack.push_back(nums[i]);
        }
        out+=stack[0];
        return su-out;
    }
};