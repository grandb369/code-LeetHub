class Solution {
public:
    bool fill(vector<vector<int>>& grid1, vector<vector<int>>&grid2, int r,int c, int n,int m)
    {
        if(r>=0 && r<n && c>=0 && c<m && grid2[r][c]==1)
        {
            grid2[r][c]=0;
            bool out = grid1[r][c]==1?true:false;
            out=fill(grid1,grid2,r-1,c,n,m)&&out;
            out=fill(grid1,grid2,r+1,c,n,m)&&out;
            out=fill(grid1,grid2,r,c-1,n,m)&&out;
            out=fill(grid1,grid2,r,c+1,n,m)&&out;
            return out;
        }
        return true;
    }
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int out=0;
        int n=grid1.size();
        int m=grid1[0].size();
        for (int r=0;r<n;r++)
        {
            for (int c=0;c<m;c++)
            {
                if (grid2[r][c]==1 && fill(grid1,grid2,r,c,n,m))
                {
                    out++;
                }
            }
        }
        return out;
    }
};