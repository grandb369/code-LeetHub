class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& mat) {
        int n=mat.size(),m=mat[0].size();
        vector<vector<int>>out(m,vector<int>(n,0));
        int r,c;
        for(r=0;r<n;r++)
        {
            for(c=0;c<m;c++)
            {
                out[c][r]=mat[r][c];
            }
        }
        return out;
    }
};