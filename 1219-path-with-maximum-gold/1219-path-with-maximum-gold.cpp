class Solution {
public:
    int search(vector<vector<int>>& mat, int r, int c, int n, int m){
        if(0>r || r>=n || 0>c || c>=m || mat[r][c]==0)return 0;
        int val=mat[r][c];
        mat[r][c]=0;
        int res=val;
        res=max(res, val+search(mat,r-1,c,n,m));
        res=max(res, val+search(mat,r+1,c,n,m));
        res=max(res, val+search(mat,r,c-1,n,m));
        res=max(res, val+search(mat,r,c+1,n,m));
        mat[r][c]=val;
        return res;
    }
    int getMaximumGold(vector<vector<int>>& mat) {
        int n=mat.size();
        int m=mat[0].size();
        int out=0;
        for(int r=0;r<n;r++){
            for(int c=0;c<m;c++){
                out=max(out,search(mat,r,c,n,m));
            }
        }
        return out;
    }
};