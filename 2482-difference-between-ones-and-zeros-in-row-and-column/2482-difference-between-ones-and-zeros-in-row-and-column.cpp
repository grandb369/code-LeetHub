class Solution {
public:
    vector<vector<int>> onesMinusZeros(vector<vector<int>>& mat) {
        int r=0;
        int c=0;
        int n=mat.size();
        int m=mat[0].size();
        int i,j;
        for(i=0;i<n;i++){
            for(j=0;j<m;j++){
                int val=mat[i][j]==1?1:-1;
                if(i==0 || j==0)mat[i][j]=0;
                if(i==0 && j==0){
                    r+=val;
                    c+=val;
                }
                else if(i==0){
                    r+=val;
                    mat[0][j]+=val;
                }
                else if(j==0){
                    c+=val;
                    mat[i][0]+=val;
                }
                else{
                    mat[i][0]+=val;
                    mat[0][j]+=val;
                }
            }
        }
        for(i=n-1;i>=0;i--){
            for(j=m-1;j>=0;j--){
                if(i==0 && j==0){
                    mat[0][0]=r+c;
                }
                else if(i==0){
                    mat[i][j]+=r;
                }
                else if(j==0){
                    mat[i][j]+=c;
                }
                else{
                    mat[i][j]=mat[i][0]+mat[0][j];
                }
            }
        }
        return mat;
    }
};