struct com{
    bool operator()(const vector<int>&a, const vector<int>&b)
    {
        return a[0]>b[0];
    }
};
class Solution {
public:
    int kthSmallest(vector<vector<int>>& mat, int k) {
        priority_queue<vector<int>,vector<vector<int>>, com>temp;
        int out=mat[0][0];
        int n=mat.size();
        int m=mat[0].size();
        temp.push({mat[0][0],0,0});
        while (k>0)
        {
            k--;
            vector<int>cur=temp.top();
            temp.pop();
            out=cur[0];
            int r=cur[1];
            int c=cur[2];
            if (r+1<n)
            {
                temp.push({mat[r+1][c],r+1,c});
            }
            if(c+1<m && r==0)
            {
                temp.push({mat[r][c+1],r,c+1});
            }
        }
        return out;
    }
};