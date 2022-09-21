class Solution {
public:
    vector<int> sumEvenAfterQueries(vector<int>& nums, vector<vector<int>>& q) {
        int out=0;
        vector<int>ans;
        for(int i:nums)
        {
            if (i%2==0)
            {
                out+=i;
            }
        }
        for(int i=0;i<q.size();i++)
        {
            int val=nums[q[i][1]];
            int v=q[i][0];
            if(val%2==0)
            {
                out-=val;
            }
            nums[q[i][1]]+=v;
            if(abs(val%2)==abs(v%2))
            {
                out+=nums[q[i][1]];
            }
            ans.push_back(out);
        }
        return ans;
    }
};