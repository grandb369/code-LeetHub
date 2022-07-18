class Solution {
public:
    void backtrack(vector<vector<int>>&out, vector<int>nums, vector<int>temp, int v, int t)
    {
        if(v==t)
        {
            out.push_back(temp);
        }
        else
        {
            while(nums.size()>0)
            {
                int val=nums.back();
                if(val+v<=t)
                {
                    temp.push_back(val);
                    backtrack(out,nums,temp,v+val,t);
                    temp.pop_back();
                }
                nums.pop_back();
            }
        }
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int t) {
        vector<vector<int>>out;
        backtrack(out,nums,vector<int>{},0,t);
        return out;
    }
};