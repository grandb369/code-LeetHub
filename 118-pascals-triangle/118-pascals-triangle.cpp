class Solution {
public:
    vector<vector<int>> generate(int n) {
        vector<vector<int>>out;
        vector<int>pre{1};
        out.push_back(pre);
        for(int i=1;i<n;i++)
        {
            vector<int>cur{1};
            for(int j=0;j<pre.size()-1;j++)
            {
                cur.push_back(pre[j]+pre[j+1]);
            }
            cur.push_back(1);
            out.push_back(cur);
            pre=cur;
        }
        return out;
    }
};