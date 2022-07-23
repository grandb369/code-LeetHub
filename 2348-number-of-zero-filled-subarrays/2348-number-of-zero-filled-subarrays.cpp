class Solution {
public:
    long long zeroFilledSubarray(vector<int>& nums) {
        long long out=0;
        long c=0;
        for(int i: nums)
        {
            c=i==0?c+1:0;
            out+=c;
        }
        return out;
    }
};