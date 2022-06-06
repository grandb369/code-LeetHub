class Solution {
public:
    int specialArray(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int n=nums.size();
        int pre=0;
        for(int i=0;i<n;i++)
        {
            int val =n-i;
            if(val<=nums[i] && val>pre)return val;
            pre=nums[i];
        }
        return -1;
    }
};