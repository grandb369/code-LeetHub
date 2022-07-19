class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n=nums.size();
        int out=0;
        map<int,int>temp;
        temp[0]=1;
        int val=0;
        for(int i:nums)
        {
            val+=i;
            if(temp.find(val-k)!=temp.end())
            {
                out+=temp[val-k];
            }
            temp[val]++;
        }
        return out;
    }
};