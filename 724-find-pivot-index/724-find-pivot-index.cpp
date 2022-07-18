class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int n=nums.size();
        vector<int>left(n,0),right(n,0);
        int i;
        for(i=0;i<n;i++)
        {
            left[i]+=nums[i];
            if(i>0)left[i]+=left[i-1];
            right[n-i-1]+=nums[n-i-1];
            if(i>0)right[n-i-1]+=right[n-i];
        }
        int l,r;
        for(i=0;i<n;i++)
        {
            l=0;
            if(i>0)l+=left[i-1];
            r=0;
            if(i<n-1)r+=right[i+1];
            if(l==r)return i;
        }
        return -1;
    }
};