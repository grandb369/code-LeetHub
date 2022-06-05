class Solution {
public:
    bool check(vector<string>&temp, int r, int c, int n)
    {
        for(int i=0;i<=r;i++)
        {
            if(temp[i][c]=='Q')return false;
        }
        int x=r;
        int y=c;
        while (x>=0 && y<n)
        {
            if(temp[x][y]=='Q')return false;
            x--;
            y++;
        }
        x=r;
        y=c;
        while(x>=0 && y>=0)
        {
            if(temp[x][y]=='Q')return false;
            x--;
            y--;
        }
        return true;
    }
    void dfs(vector<vector<string>>&out, vector<string> temp, int r, int n)
    {
        if(r==n)out.push_back(temp);
        else
        {
            for(int i=0;i<n;i++)
            {
                if(check(temp,r,i,n))
                {
                    temp[r][i]='Q';
                    dfs(out,temp,r+1,n);
                    temp[r][i]='.';
                }
            }
        }
    }
    int totalNQueens(int n) {
        vector<vector<string>>out;
        dfs(out,vector<string>(n,string(n,'.')),0,n);
        return out.size();
    }
};