class Solution {
public:
    int numTeams(vector<int>& nums) {
        int n=nums.size();
        vector<int>more(n,0);
        vector<int>less(n,0);
        int out=0;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<i;j++)
            {
                if(nums[i]>nums[j])
                {
                    less[i]+=1;
                    out+=less[j];
                }
                if(nums[i]<nums[j])
                {
                    more[i]+=1;
                    out+=more[j];
                }
            }
        }
        return out;
    }
};