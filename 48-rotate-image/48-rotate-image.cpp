class Solution {
public:
    void rotate(vector<vector<int>>& mat) {
        int n=mat.size();
        for (int r=0;r<mat.size()-1;r++)
        {
            for (int c=r;c<mat.size()-r-1;c++)
            {
                int temp=mat[r][c];
                mat[r][c]=mat[n-c-1][r];
                mat[n-c-1][r]=mat[n-r-1][n-c-1];
                mat[n-r-1][n-c-1]=mat[c][n-r-1];
                mat[c][n-r-1]=temp;
            }
        }
    }
};