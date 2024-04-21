class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        map<int,set<int>>g;
        for(auto cur:edges){
            int u=cur[0];
            int v=cur[1];
            g[u].insert(v);
            g[v].insert(u);
        }
        set<int>seen{source};
        set<int>stack{source};
        while(stack.size()>0){
            set<int>temp;
            for(int i:stack)
            {
                if(i==destination)return true;
                for(int j:g[i])
                {
                    if (seen.find(j)==seen.end()){
                        seen.insert(j);
                        temp.insert(j);
                    }
                }
            }
            stack=temp;
        }
        return false;
    }
};