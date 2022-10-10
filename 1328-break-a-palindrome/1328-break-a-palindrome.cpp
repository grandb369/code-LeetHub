class Solution {
public:
    string breakPalindrome(string s) {
        if (s.size()==1)return "";
        int n=s.size();
        for(int i=0;i<n/2;i++)
        {
            if(s[i]!='a')
            {
                s[i]='a';
                return s;
            }
        }
        s[n-1]='b';
        return s;
    }
};