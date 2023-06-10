class Solution {
public:
    char nextGreatestLetter(vector<char>& nums, char target) {
        int l=0;
        int r=nums.size();
        while(l<r)
        {
            int mid=(int)(l+r)/2;
            if(nums[mid]<=target)l=mid+1;
            else r=mid;
        }
        return nums[l%nums.size()];
    }
};