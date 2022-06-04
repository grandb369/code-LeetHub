class Solution {
public:
    int firstUniqChar(string s) {
        map<int,vector<int>>out;
        for(int i=0;i<s.size();i++)
        {
            if(out.find(s[i])==out.end())
            {
                out[s[i]]=vector<int>{};
            }
            out[s[i]].push_back(i);
        }
        map<int,vector<int>>::iterator it;
        int ans=s.size();
        for(it=out.begin();it!=out.end();it++)
        {
            if(it->second.size()==1)
            {
                ans=min(ans,it->second[0]);
            }
        }
        return ans==s.size()?-1:ans;
    }
};