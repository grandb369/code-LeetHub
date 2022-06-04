class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int ma=1;
        int mi=1;
        int out=-20000;
        for(int i:nums)
        {
            int temp_ma=ma*i;
            int temp_mi=mi*i;
            ma=max(temp_ma,temp_mi);
            mi=min(temp_ma,temp_mi);
            ma=max(i,ma);
            mi=min(i,mi);
            out=max(ma,out);
        }
        return out;
    }
};