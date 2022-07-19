class Solution {
public:
    void check(vector<vector<int>>& mat,int r, int c, int n, int m, vector<int>&row2, vector<int>& col2){
        if(0<=r && r<n && 0<=c && c<m && mat[r][c]==0)
        {
            mat[r][c]=1;
            row2.push_back(r);
            col2.push_back(c);
        }
    }
    int shortestPathBinaryMatrix(vector<vector<int>>& mat) {
        int out=1;
        if(mat[0][0]==1)return -1;
        vector<int>row{0};
        vector<int>col{0};
        mat[0][0]=0;
        int n=mat.size();
        int m=mat[0].size();
        while (row.size()>0)
        {
            vector<int>row2;
            vector<int>col2;
            for(int i=0;i<row.size();i++)
            {
                int r=row[i];
                int c=col[i];
                if(r==n-1 && c==m-1)return out;
                check(mat,r-1,c-1,n,m,row2,col2);
                check(mat,r-1,c,n,m,row2,col2);
                check(mat,r-1,c+1,n,m,row2,col2);
                check(mat,r,c-1,n,m,row2,col2);
                check(mat,r,c+1,n,m,row2,col2);
                check(mat,r+1,c-1,n,m,row2,col2);
                check(mat,r+1,c,n,m,row2,col2);
                check(mat,r+1,c+1,n,m,row2,col2);
            }
            row=row2;
            col=col2;
            out++;
        }
        return -1;
    }
};