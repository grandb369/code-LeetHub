class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n=nums.size();
        int out=-30000;
        int negout=30000;
        int su=0;
        int ma=-30000;
        int mi=30000;
        for(int i:nums)
        {
            ma=max(ma+i,i);
            out=max(out,ma);
            mi=min(mi+i,i);
            negout=min(negout,mi);
            su+=i;
        }
        return out>0?max(out,su-negout):out;
        
    }
};