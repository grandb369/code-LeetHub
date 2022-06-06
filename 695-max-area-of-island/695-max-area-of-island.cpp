class Solution {
public:
    int fill(vector<vector<int>>& mat, int r, int c)
    {
        if(r>=0 && r<mat.size() && c>=0 && c<mat[0].size() && mat[r][c]==1)
        {
            mat[r][c]=0;
            int out=1;
            out+=fill(mat,r-1,c);
            out+=fill(mat,r+1,c);
            out+=fill(mat,r,c-1);
            out+=fill(mat,r,c+1);
            return out;
        }
        return 0;
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int out=0;
        for(int r=0;r<grid.size();r++)
        {
            for (int c=0;c<grid[0].size();c++)
            {
                if(grid[r][c]==1)out=max(out,fill(grid,r,c));
            }
        }
        return out;
    }
};