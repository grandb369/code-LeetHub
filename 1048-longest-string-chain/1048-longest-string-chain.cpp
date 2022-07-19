class Solution {
public:
    int longestStrChain(vector<string>& ss) {
        map<int,vector<string>,greater<int>>k;
        map<string,int>ans;
        int out=1;
        for(string s:ss)
        {
            ans[s]=1;
            k[s.size()].push_back(s);
        }
        for(auto it:k)
        {
            if(k.find(it.first-1)!=k.end())
            {
                for(string s:it.second)
                {
                    for(int j=0;j<s.size();j++)
                    {
                        string l=s.substr(0,j);
                        string r=s.substr(j+1);
                        string temp=l+r;
                        if(ans.find(temp)!=ans.end())
                        {
                            ans[temp]=max(ans[temp],ans[s]+1);
                            out=max(out,ans[temp]);
                        }
                    }
                }
            }
        }
        return out;
        
    }
};