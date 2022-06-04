class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char,int>temp(26);
        if (s.size()!=t.size())return false;
        for(char i:s)
        {
            temp[i]++;
        }
        for(char i:t)
        {
            temp[i]--;
            if(temp[i]<0)return false;
        }
        return true;
    }
};