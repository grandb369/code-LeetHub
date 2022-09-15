class Solution {
public:
    vector<int> findOriginalArray(vector<int>& nums) {
        unordered_map<int,int>temp;
        vector<int>out;
        sort(nums.begin(),nums.end());
        
        for(int i:nums)
        {
            if(i%2==0 && temp[i/2]!=0)
            {
                out.push_back(i/2);
                temp[i/2]--;
            }
            else
            {
                temp[i]++;
            }
        }
        return out.size()*2==nums.size()?out:vector<int>{};
    }
};