class Solution {
public:
    int removePalindromeSub(string s) {
        if(s.size()==0)return 0;
        string ss=s;
        reverse(ss.begin(),ss.end());
        if (ss==s)return 1;
        return 2;
    }
};