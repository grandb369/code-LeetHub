class Solution {
public:
    int minimumTotal(vector<vector<int>>& nums) {
        int n=nums.size();
        for (int r=1;r<n;r++)
        {
            for(int c=0;c<nums[r].size();c++)
            {
                if (c-1>=0 && c<nums[r-1].size())
                {
                    nums[r][c]+=min(nums[r-1][c],nums[r-1][c-1]);
                }
                else if(c-1>=0)
                {
                    nums[r][c]+=nums[r-1][c-1];
                }
                else
                {
                    nums[r][c]+=nums[r-1][c];
                }
            }
        }
        
        int out=nums[n-1][0];
        for(int c=1;c<nums[n-1].size();c++)
        {
            out=min(out,nums[n-1][c]);
        }
        return out;
    }
};