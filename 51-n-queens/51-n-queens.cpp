class Solution {
public:
    void back(vector<vector<string>>&out, int r, int n, vector<string>&temp)
    {
        if(r==n)out.push_back(temp);
        else
        {
            for(int c=0;c<n;c++)
            {
                int x=r-1;
                int y;
                bool flag=true;
                while(x>=0)
                {
                    if(temp[x][c]=='Q')flag=false;
                    x--;
                }
                if(!flag)continue;
                x=r-1;
                y=c-1;
                while(x>=0 && y>=0)
                {
                    if(temp[x][y]=='Q')flag=false;
                    x--;
                    y--;
                }
                if(!flag)continue;
                x=r-1;
                y=c+1;
                while(x>=0 && y<n)
                {
                    if(temp[x][y]=='Q')flag=false;
                    x--;
                    y++;
                }
                if(!flag)continue;
                temp[r][c]='Q';
                back(out,r+1,n,temp);
                temp[r][c]='.';
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>>out;
        vector<string>temp(n,string(n,'.'));
        back(out,0,n,temp);
        return out;
    }
};