class Solution {
public:
    bool check(vector<vector<int>>&mat, int r, int c, int n, int m){
        for(auto i:vector<vector<int>>{{0,1},{0,-1},{1,0},{-1,0}}){
            int x=r+i[0];
            int y=c+i[1];
            if(x>=0 and x<n and y>=0 and y<m and mat[x][y]==0)return true;
        }
        return false;
    }
    void get(vector<vector<int>>&mat, int r, int c, int n, int m, map<vector<int>,int>&temp,set<vector<int>>&nex){
        for(auto i:vector<vector<int>>{{0,1},{0,-1},{1,0},{-1,0}}){
            int x=r+i[0];
            int y=c+i[1];
            if(x>=0 and x<n and y>=0 and y<m){
                if (temp.find({x,y})==temp.end()){
                    nex.insert({x,y});
                    mat[x][y]=mat[r][c]+1;
                    temp[{x,y}]=mat[x][y];
                }
            }
        }
    }
    vector<vector<int>> updateMatrix(vector<vector<int>>& mat) {
        map<vector<int>,int>temp;
        int r,c;
        int n=mat.size();
        int m=mat[0].size();
        set<vector<int>>stack;
        for(r=0;r<n;r++){
            for(c=0;c<m;c++)
            {
                if(mat[r][c]==0){
                    temp[{r,c}]=0;
                }
                else if(check(mat,r,c,n,m)){
                    temp[{r,c}]=1;
                    stack.insert({r,c});
                }
            }
        }
        
        while(stack.size()>0){
            set<vector<int>>nex;
            for(auto i:stack){
                r=i[0];
                c=i[1];
                get(mat,r,c,n,m,temp,nex);
            }
            stack=nex;
            
        }
        return mat;
    }
};