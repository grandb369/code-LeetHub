class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int>temp;
        for(int i:nums)temp.push(i);
        int out=nums[0];
        while(k>0)
        {
            out=temp.top();
            temp.pop();
            k--;
        }
        return out;
    }
};