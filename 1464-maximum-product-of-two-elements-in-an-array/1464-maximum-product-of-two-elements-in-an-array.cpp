class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int v1=nums[0];
        int v2=nums[1];
        if(v1<v2){
            v1=v2;
            v2=nums[0];
        }
        for(int i=2;i<nums.size();i++){
            if(nums[i]>v1){
                v2=v1;
                v1=nums[i];
            }
            else if(nums[i]==v1)v2=v1;
            else if(nums[i]>v2)v2=nums[i];
        }
        return (v2-1)*(v1-1);
    }
};