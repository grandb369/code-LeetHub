class Solution {
public:
    void dfs(vector<vector<string>>&out, vector<string> temp, set<int> x, set<int>dia, set<int> ndia ,int r, int n)
    {
        if(r==n)out.push_back(temp);
        else
        {
            for(int i=0;i<n;i++)
            {
                if (x.find(i)!=x.end())continue;
                if (dia.find(i-r)!=dia.end())continue;
                if (ndia.find(i+r)!=ndia.end())continue;
                set<int> newx{i};
                set<int> newdia{i-r};
                set<int> newndia{i+r};
                newx.insert(x.begin(),x.end());
                newdia.insert(dia.begin(),dia.end());
                newndia.insert(ndia.begin(),ndia.end());
                vector<string> nex=temp;
                nex.push_back(string(i,'.')+'Q'+string(n-1-i,'.'));
                dfs(out,nex,newx,newdia,newndia,r+1,n);
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>>out;
        dfs(out,vector<string>{},set<int>{},set<int>{},set<int>{},0,n);
        return out;
    }
};