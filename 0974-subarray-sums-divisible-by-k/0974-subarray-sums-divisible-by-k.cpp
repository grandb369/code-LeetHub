class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        int n=nums.size();
        map<int,int>temp;
        temp[0]=1;
        int out=0;
        for(int i=0;i<n;i++)
        {
            if(i>0)nums[i]+=nums[i-1];
            nums[i]=(nums[i]%k+k)%k;
            out+=temp[nums[i]];
            temp[nums[i]]++;
        }
        return out;
    }
};