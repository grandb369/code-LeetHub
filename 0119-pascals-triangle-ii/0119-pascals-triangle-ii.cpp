class Solution {
public:
    vector<int> getRow(int row) {
        vector<int> out;
        out.push_back(1);
        
        if(row==0)return out;
        
        int cur = row;
        out.push_back(cur);
        
        int n = row-1;
        int r = 2;
        
        for(int i=0;i<row-1;i++)
        {
            cur = (long)cur*n/r;
            out.push_back(cur);
            n--;
            r++;
        }
        return out;
    }
};