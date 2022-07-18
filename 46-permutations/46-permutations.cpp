class Solution {
public:
    void backtrack(vector<vector<int>>& out, vector<int>temp, vector<int>nums)
    {
        if(nums.size()==0)
        {
            out.push_back(temp);
        }
        else
        {
            vector<int>save;
            int n=nums.size();
            for(int i=0;i<n;i++)
            {
                int val=nums[n-i-1];
                temp.push_back(val);
                nums.pop_back();
                while (save.size()>0)
                {
                    nums.push_back(save.back());
                    save.pop_back();
                }
                backtrack(out,temp,nums);
                temp.pop_back();
                for(int j=0;j<i;j++)
                {
                    save.push_back(nums.back());
                    nums.pop_back();
                }
                save.push_back(val);
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>>out;
        vector<int>temp;
        backtrack(out,temp,nums);
        return out;
    }
};