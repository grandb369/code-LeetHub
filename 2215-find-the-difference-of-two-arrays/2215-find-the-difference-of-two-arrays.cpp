
class Solution {
public:
    bool check(vector<int> nums, int i){
        if (std::find(nums.begin(),nums.end(),i) == nums.end())return true;
        return false;
    }
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<int>temp;
        vector<int>temp2;
        for(int i:nums1){
            if(check(nums2,i) && check(temp,i)) temp.push_back(i);
        }
        for(int i:nums2){
            if(check(nums1,i) && check(temp2,i)) temp2.push_back(i);
        }
        return vector<vector<int>>{temp,temp2};
    }
};