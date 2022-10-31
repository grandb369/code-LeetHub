class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& mat) {
        int n=mat.size();
        int m=mat[0].size();
        for(int i=0;i<n;i++)
        {
            int c=0;
            int r=i;
            int val=mat[r][c];
            while(r<n && c<m)
            {
                if(mat[r][c]!=val)return false;
                r++;
                c++;
            }
        }
        for(int i=1;i<m;i++)
        {
            int r=0;
            int c=i;
            int val=mat[r][c];
            while(r<n && c<m)
            {
                if(mat[r][c]!=val)return false;
                r++;
                c++;
            }
        }
        return true;
    }
};