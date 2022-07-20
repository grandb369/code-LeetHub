class Solution {
public:
    map<int,vector<int>>data;
    Solution(vector<int>& nums) {
        for(int i=0;i<nums.size();i++)
        {
            data[nums[i]].push_back(i);
        }
    }
    
    int pick(int target) {
        int val=rand()%data[target].size();
        return data[target][val];
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */