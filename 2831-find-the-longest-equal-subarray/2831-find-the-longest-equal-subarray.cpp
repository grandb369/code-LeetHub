class Solution {
public:
    int longestEqualSubarray(vector<int>& nums, int k) {
        map<int,int>temp;
        int out=0;
        int i=0;
        for(int j=0;j<nums.size();j++){
            out=max(out,++temp[nums[j]]);
            if(j-i+1-out>k){
                --temp[nums[i++]];
            }
        }
        return out;
    }
};