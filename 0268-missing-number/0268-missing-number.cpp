class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int _n=-1;
        int n=nums.size();
        for (int i=0;i<n;i++){
            while (nums[i]!=n && nums[i]!=i)
            {
                int temp=nums[i];
                nums[i]=nums[temp];
                nums[temp]=temp;
            }
            if (nums[i]==n)
            {
                _n=i;
            }
        }
        if (_n==-1)return n;
        return _n;
    }
};