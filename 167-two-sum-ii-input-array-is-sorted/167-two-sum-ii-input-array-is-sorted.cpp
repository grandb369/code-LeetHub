class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int t) {
        int l=0;
        int r=nums.size()-1;
        while(l<r)
        {
            int val=nums[l]+nums[r];
            if(val==t)return vector<int>{l+1,r+1};
            else if(val>t)r--;
            else l++;
        }
        return vector<int>{l,r};
    }
};