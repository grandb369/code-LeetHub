class Solution {
public:
    vector<vector<int>> findWinners(vector<vector<int>>& nums) {
        map<int,int>temp;
        set<int>num;
        vector<vector<int>>out(2,vector<int>{});
        for(int i=0;i<nums.size();i++){
            temp[nums[i][1]]++;
            num.insert(nums[i][0]);
            num.insert(nums[i][1]);
        }
        for(int i:num)
        {
            if(temp[i]==0)out[0].push_back(i);
            else if(temp[i]==1)out[1].push_back(i);
        }
        sort(out[0].begin(),out[0].end());
        sort(out[1].begin(),out[1].end());
        return out;
        
    }
};