class Solution {
public:
    long long maximumHappinessSum(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int d=0;
        long long out=0;
        while(k>0){
            int cur=nums.back();
            nums.pop_back();
            if (d>=cur)break;
            out+=(cur-d);
            d++;
            k--;
        }
        return out;
    }
};