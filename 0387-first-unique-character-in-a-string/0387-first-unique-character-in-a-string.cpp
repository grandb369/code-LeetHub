class Solution {
public:
    int firstUniqChar(string s) {
                unordered_map<char,int>temp;
        for(char c:s)
        {
            temp[c]++;
        }
        for(int i=0;i<s.size();i++)
        {
            if(temp[s[i]]==1)return i;
        }
        return -1;
    }
};