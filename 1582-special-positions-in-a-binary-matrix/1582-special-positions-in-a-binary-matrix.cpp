class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int n=mat.size();
        int m=mat[0].size();
        map<int,vector<int>>row;
        map<int,int>col;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(mat[i][j]==1){
                    row[i].push_back(j);
                    col[j]++;
                }
            }
        }
        int out=0;
        for(auto lt=row.begin();lt!=row.end();lt++){
            if(lt->second.size()==1 && col[lt->second[0]]==1)out++;
        }
        return out;
    }
};