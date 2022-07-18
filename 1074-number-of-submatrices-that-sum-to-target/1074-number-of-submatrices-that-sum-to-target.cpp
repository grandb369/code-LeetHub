class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& mat, int t) {
        int r,c;
        int x,y;
        int n=mat.size(),m=mat[0].size();
        int out=0;
        for(r=0;r<n;r++)
        {
            for(c=1;c<m;c++)
            {
                mat[r][c]+=mat[r][c-1];
            }
        }
        int c1,c2;
        
        for(c1=0;c1<m;c1++)
        {
            for(c2=c1;c2<m;c2++)
            {
                unordered_map<int,int>temp;
                temp[0]=1;
                int pre=0;
                for(r=0;r<n;r++)
                {
                    pre+=mat[r][c2];
                    if(c1>0)pre-=mat[r][c1-1];
                    if(temp.find(pre-t)!=temp.end())
                    {
                        out+=temp[pre-t];
                    }
                    temp[pre]++;
                }
            }
        }
    
        return out;
        
    }
};