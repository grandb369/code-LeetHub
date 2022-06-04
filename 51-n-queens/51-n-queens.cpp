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
                x.insert(i);
                dia.insert(i-r);
                ndia.insert(i+r);
                temp.push_back(string(i,'.')+'Q'+string(n-1-i,'.'));
                dfs(out,temp,x,dia,ndia,r+1,n);
                temp.pop_back();
                x.erase(i);
                dia.erase(i-r);
                ndia.erase(i+r);
            }
        }
    }
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>>out;
        dfs(out,vector<string>{},set<int>{},set<int>{},set<int>{},0,n);
        return out;
    }
};