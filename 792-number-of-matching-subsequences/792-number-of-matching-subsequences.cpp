class Solution {
public:
    int numMatchingSubseq(string s, vector<string>& words) {
        map<char,vector<string>>temp;
        int out=0;
        for(string w:words)
        {
            temp[w[0]].push_back(w);
        }
        for(char c:s)
        {
            vector<string>cur=temp[c];
            temp[c]={};
            for(string ss:cur)
            {
                if(ss.size()==1)
                {
                    out++;
                }
                else
                {
                    temp[ss[1]].push_back(ss.substr(1));
                }
            }
        }
        return out;
    }
};