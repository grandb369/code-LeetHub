class Solution {
public:
    string customSortString(string order, string str) {
        unordered_map<char,int>k;
        for (char i:str)
        {
            if (k.find(i)==k.end())
            {
                k[i]=0;
            }
            k[i]++;
        }
        string out="";
        for (char i:order)
        {
            if (k.find(i)!=k.end())
            {
                out+=string(k[i], i);
                k.erase(i);
            }
        }
        for (auto i:k)
        {
            out+=string(i.second, i.first);
        }
        return out;
    }
};