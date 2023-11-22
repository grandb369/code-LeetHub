class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& nums) {
        map<int,vector<int>> temp;
        int n=nums.size();
        int r,c;
        int m=0;
        for(r=n-1;r>=0;r--){
            for(c=0;c<nums[r].size();c++){
                temp[r+c].push_back(nums[r][c]);
                m=max(m,r+c);
            }
        }
        vector<int>out;
        for(r=0;r<m+1;r++){
            out.insert(out.end(),temp[r].begin(), temp[r].end());
        }
        return out;
    }
};