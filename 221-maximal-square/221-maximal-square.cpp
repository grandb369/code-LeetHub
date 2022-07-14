#include <algorithm>
class Solution {
public:
    int maximalSquare(vector<vector<char>>& mat) {
        int r,c;
        int n,m;
        n=mat.size();
        m=mat[0].size();
        int out=0;
        vector<vector<int>>temp(n,vector<int>(m,0));
        for(r=0;r<n;r++)
        {
            temp[r][0]=mat[r][0]=='1'?1:0;
            out=max(out,temp[r][0]);
        }
        for(c=1;c<m;c++)
        {
            temp[0][c]=mat[0][c]=='1'?1:0;
            out=max(out,temp[0][c]);
        }
        for(r=1;r<n;r++)
        {
            for(c=1;c<m;c++)
            {
                if(mat[r][c]=='0')
                {
                    temp[r][c]=0;
                }
                else
                {
                    temp[r][c]=min(temp[r-1][c-1],min(temp[r][c-1],temp[r-1][c]))+1;
                }
                out=max(out,temp[r][c]);
            }
        }
        return out*out;
    }
};