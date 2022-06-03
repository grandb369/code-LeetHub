class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int l=0;
        int r=nums.size();
        vector<int>out{-1,-1};
        while (l<r)
        {
            int mid = (int)(l+r)/2;
            if (nums[mid]>=target)r=mid;
            else l=mid+1;
        }
        if (l==nums.size()|| nums[l]!=target)return out;
        out[0]=l;
        l=0;
        r=nums.size();
        while(l<r)
        {
            int mid = (int)(l+r)/2;
            if(nums[mid]<=target)l=mid+1;
            else r=mid;
        }
        if(l==nums.size()||nums[l]!=target)l--;
        out[1]=l;
        return out;
    }
};