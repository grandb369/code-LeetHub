class Solution {
public:
    bool closeStrings(string s1, string s2) {
        if (s1.size()!=s2.size())return false;
        map<char,int>temp1;
        map<char,int>temp2;
        set<char> k1;
        set<char> k2;
        for(char c:s1){temp1[c]++;k1.insert(c);}
        for(char c:s2){temp2[c]++;k2.insert(c);}
        if (k1!=k2)return false;
        vector<int>out1;
        vector<int>out2;
        for(auto lt:temp1)out1.push_back(lt.second);
        for(auto lt:temp2)out2.push_back(lt.second);
        sort(out1.begin(),out1.end());
        sort(out2.begin(),out2.end());
        return out1==out2;
    }
};