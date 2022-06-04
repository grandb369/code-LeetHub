class Solution {
public:
    bool check(vector<vector<char>>& mat, map<int,set<char>>& ver, map<int,set<char>>& hor, map<int,set<char>>& grid, int r,int c)
    {
        char val=mat[r][c];
        if(ver[r].find(val)!=ver[r].end())return false;
        if(hor[c].find(val)!=hor[c].end())return false;
        int g=(int)(r/3)*3+(int)c/3;
        if(grid[g].find(val)!=grid[g].end())return false;
        ver[r].insert(val);
        hor[c].insert(val);
        grid[g].insert(val);
        return true;
    }
    bool isValidSudoku(vector<vector<char>>& mat) {
        map<int,set<char>>ver;
        map<int,set<char>>hor;
        map<int,set<char>>grid;
        for(int r=0;r<mat.size();r++)
        {
            for (int c=0;c<mat[0].size();c++)
            {
                if(mat[r][c]!='.' && !check(mat,ver,hor,grid,r,c))return false;
            }
        }
        return true;
    }
};