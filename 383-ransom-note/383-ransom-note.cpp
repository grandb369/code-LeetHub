class Solution {
public:
    bool canConstruct(string r, string m) {
        map<char,int>temp;
        for(char s:m)
        {
            if(temp.find(s)==temp.end())temp[s]=0;
            temp[s]++;
        }
        for(char s:r)
        {
            if(temp.find(s)==temp.end())return false;
            if(temp[s]==0)return false;
            temp[s]--;
        }
        return true;
    }
};