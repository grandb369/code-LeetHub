class Solution {
public:
    int maximalRectangle(vector<vector<char>>& mat) {
        int r,c;
        int n=mat.size();
        int m=mat[0].size();
        vector<int>stack;
        vector<int>cur(m+2,0);
        vector<int>pre(m+2,0);
        int out=0;
        for(r=0;r<n;r++)
        {
            for(c=0;c<m+2;c++)
            {
                if(c<m)
                {
                    if(mat[r][c]=='0')
                    {
                        cur[c+1]=0;
                    }
                    else
                    {
                        cur[c+1]=pre[c+1]+1;
                    }
                }     
                while(stack.size()>0 && cur[stack.back()]>cur[c])
                {
                    int index=stack.back();
                    stack.pop_back();
                    out=max(out,cur[index]*(c-stack.back()-1));
                }
                stack.push_back(c);
            }
            pre=cur;
            stack.clear();
        }
        return out;
    }
};
