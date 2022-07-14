class Solution {
public:
    int largestRectangleArea(vector<int>& nums) {
        int out=0;
        vector<int>stack{0};
        vector<int>temp;
        int i,last;
        for(i=0;i<nums.size();i++)
        {
            stack.push_back(nums[i]);
        }
        stack.push_back(0);
        for(i=0;i<stack.size();i++)
        {
            while(temp.size()>0 && stack[temp.back()]>stack[i])
            {
                last=temp.back();
                temp.pop_back();
                out=max(out,stack[last]*(i-temp.back()-1));
            }
            temp.push_back(i);
        }
        return out;
    }
};