class Solution {
public:
    int check(int a, int b, int c)
    {
        if(a+b<=c)return 0;
        if(a+c<=b)return 0;
        if(b+c<=a)return 0;
        return a+b+c;
    }
    int largestPerimeter(vector<int>& nums) {
        int out=0;
        sort(nums.begin(),nums.end());
        for (int i=nums.size()-1;i>1;i--)
        {
            int val=check(nums[i],nums[i-1],nums[i-2]);
            if (val!=0)return val;
        }
        return out;
    }
};