class Solution {
public:
    int trap(vector<int>& nums) {
        int l=0;
        int r=nums.size()-1;
        int out=0;
        while (l<r)
        {
            while(l<r && nums[l]<nums[l+1])
            {
                l++;
            }
            while(l<r && nums[r]<nums[r-1])
            {
                r--;
            }
            if(l==r)break;
            if(nums[l]<nums[r])
            {
                out+=(nums[l]-nums[l+1]);
                nums[l+1]=nums[l];
                l++;
            }
            else
            {
                out+=(nums[r]-nums[r-1]);
                nums[r-1]=nums[r];
                r--; 
            }
        }
        return out;
    }
};