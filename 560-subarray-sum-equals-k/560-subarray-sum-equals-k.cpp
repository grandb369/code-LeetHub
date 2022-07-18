class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n=nums.size();
        int i;
        unordered_map<int,int>temp;
        temp[0]=1;
        int out=0;
        for(i=0;i<nums.size();i++)
        {
            if(i>0)nums[i]+=nums[i-1];
            if(temp.find(nums[i]-k)!=temp.end())out+=temp[nums[i]-k];
            temp[nums[i]]++;
        }
        
        return out;
    }
};