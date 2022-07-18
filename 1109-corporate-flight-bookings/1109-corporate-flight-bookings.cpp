class Solution {
public:
    vector<int> corpFlightBookings(vector<vector<int>>& nums, int n) {
        vector<int>out(n,0);
        for(vector<int> cur:nums)
        {
            out[cur[0]-1]+=cur[2];
            if(cur[1]<n)out[cur[1]]-=cur[2];
        }
        int val=0;
        for(int i=0;i<n;i++)
        {
            out[i]+=val;
            val=out[i];
        }
        return out;
    }
};