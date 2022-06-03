class NumMatrix {
public:
    vector<vector<int>>data;
    NumMatrix(vector<vector<int>>& matrix) {
        data=matrix;
        int n= data.size();
        int m=data[0].size();
        for(int r=0;r<n;r++)
        {
            for(int c=0;c<m;c++)
            {
                if(r>0)data[r][c]+=data[r-1][c];
                if(c>0)data[r][c]+=data[r][c-1];
                if(r>0 && c>0)data[r][c]-=data[r-1][c-1];
            }
        }
    }
    
    int sumRegion(int r1, int c1, int r2, int c2) {
        int out =data[r2][c2];
        if(r1-1>=0)out-=data[r1-1][c2];
        if(c1-1>=0)out-=data[r2][c1-1];
        if(r1-1>=0 && c1-1>=0)out+=data[r1-1][c1-1];
        return out;
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */