class Solution {
public:
    void fill(vector<vector<int>>& mat, int r, int c, int pre, int val)
    {
        if(r>=0 && r<mat.size() && c>=0 && c<mat[0].size() && mat[r][c]==pre)
        {
            mat[r][c]=val;
            fill(mat,r+1,c,pre,val);
            fill(mat,r-1,c,pre,val);
            fill(mat,r,c-1,pre,val);
            fill(mat,r,c+1,pre,val);
        }
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int c) {
        if (image[sr][sc]==c)return image;
        fill(image,sr,sc,image[sr][sc],c);
        return image;
    }
};