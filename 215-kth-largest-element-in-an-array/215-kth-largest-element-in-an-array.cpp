class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        partial_sort(nums.rbegin(),nums.rbegin()+k,nums.rend(),std::greater{});
        return nums[nums.size()-k];
    }
};