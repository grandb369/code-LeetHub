class Solution {
public:
    bool checkPossibility(vector<int>& nums) {
        int c1=1;
        int c2=1;
        int n=nums.size()-1;
        int pre1=nums[0];
        int pre2=nums[n];
        
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]<pre1)c1--;
            else pre1=nums[i];
            if(nums[n-i]>pre2)c2--;
            else pre2=nums[n-i];
        }
        return c1>=0 || c2>=0;
    }
};