class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        unordered_map<char,string>temp;
        string p="";
        int cur=0;
        for(char c:pattern)
        {
            if(!temp.count(c))
            {
                temp[c]=to_string(cur);
                cur++;
            }
            p+=temp[c];
        }
        vector<string>out;
        for(string w:words)
        {
            temp.clear();
            cur=0;
            string s="";
            for(char c:w)
            {
                if(!temp.count(c))
                {
                    temp[c]=to_string(cur);
                    cur++;
                }
                s+=temp[c];
            }
            if (s==p)
            {
                out.push_back(w);
            }
        }
        return out;
    }
};