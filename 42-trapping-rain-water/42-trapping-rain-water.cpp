class Solution {
public:
    int trap(vector<int>& nums) {
        int n = nums.size();
        int out = 0;
        int p_left = 0;
        int p_right = n-1;

        while (p_left < p_right)
        {
            if(nums[p_left]<nums[p_right])
            {
                out += max(0,nums[p_left]-nums[p_left+1]);
                nums[p_left+1] = max(nums[p_left],nums[p_left+1]);
                p_left++;
            }
            else
            {
                out += max(0,nums[p_right]-nums[p_right-1]);
                nums[p_right-1] = max(nums[p_right],nums[p_right-1]);
                p_right--;
            }
        }
        return out;
    }
};