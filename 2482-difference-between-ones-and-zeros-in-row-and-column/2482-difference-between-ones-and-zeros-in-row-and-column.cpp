class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& mat) {
        map<int,int>row;
        map<int,int>col;
        int n=mat.size();
        int m=mat[0].size();
        int i,j;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                int val=mat[i][j]==1?1:-1;
                row[i]+=val;
                col[j]+=val;
            }
        }
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                mat[i][j]=row[i]+col[j];
            }
        }
        return mat;
    }
};