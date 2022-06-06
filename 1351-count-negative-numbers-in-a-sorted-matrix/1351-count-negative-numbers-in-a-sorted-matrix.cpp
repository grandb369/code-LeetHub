class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int out =0;
        int n=grid.size();
        int m=grid[0].size();
        int r=0;
        for(int c=m-1;c>=0;c--)
        {
            while (r<n && grid[r][c]>=0)r++;
            out+=(n-r);
            if(n==r)break;
        }
        return out;
    }
};