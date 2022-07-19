class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& nums, vector<int>& add) {
        nums.push_back(add);
        sort(nums.begin(),nums.end(),[](const vector<int>&a, const vector<int>&b)
             {
                 return a[0]<b[0];
             });
        int s=nums[0][0];
        int e=nums[0][1];
        vector<vector<int>>out;
        for(int i=1;i<nums.size();i++)
        {
            int nex_s=nums[i][0];
            int nex_e=nums[i][1];
            if(nex_s>e)
            {
                out.push_back(vector<int>{s,e});
                s=nex_s;
                e=nex_e;
            }
            else
            {
                e=max(e,nex_e);
            }
        }
        out.push_back(vector<int>{s,e});
        return out;
    }
};