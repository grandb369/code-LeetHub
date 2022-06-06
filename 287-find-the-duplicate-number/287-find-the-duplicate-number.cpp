class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int p1=nums[0];
        int p2=nums[0];
        while (true)
        {
            p1=nums[nums[p1]];
            p2=nums[p2];
            if(p1==p2)break;
        }
        p2=nums[0];
        while (p1!=p2)
        {
            p1=nums[p1];
            p2=nums[p2];
        }
        return p1;
    }
};