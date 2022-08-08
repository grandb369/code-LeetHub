class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        vector<int>temp;
        for(int i:nums)
        {
            int l=0;
            int r=temp.size();
            while(l<r)
            {
                int mid=l+(r-l)/2;
                if(temp[mid]<i)l=mid+1;
                else r=mid;
            }
            if(l>=temp.size())temp.push_back(i);
            else temp[l]=i;
        }
        return temp.size();
    }
};