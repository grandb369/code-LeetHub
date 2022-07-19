class Solution {
public:
    int threeSumSmaller(vector<int>& nums, int t) {
        int out=0;
        int n=nums.size();
        sort(nums.begin(),nums.end());
        int i,j,k;
        for(i=0;i<n-2;i++)
        {
            int v1=t-nums[i];
            j=i+1;
            while(j<n && nums[j]*2<v1)
            {
                out+=(j-i-1);
                j++;
            }
            k=j-1;
            while(k>i && j<n)
            {
                while(k>i && nums[k]+nums[j]>=v1)
                {
                    k--;
                }
                out+=(k-i);
                j++;
            }
        }
        return out;
    }
};