class Solution {
public:
    vector<int> findSmallestSetOfVertices(int n, vector<vector<int>>& edges) {
        vector<int>out;
        vector<int>temp(n,0);
        for(auto i:edges){
            int u=i[0];
            int v=i[1];
            temp[v]++;
        }
        for(int i=0;i<n;i++){
            if(temp[i]==0)out.push_back(i);
        }
        return out;
    }
};