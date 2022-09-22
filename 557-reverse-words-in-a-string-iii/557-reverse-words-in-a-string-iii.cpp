class Solution {
public:
    string reverseWords(string s) {
        string out="";
        int pre=-1;
        for(int i=0;i<s.size()+1;i++)
        {
            if(i==s.size() || s[i]==' ')
            {
                for(int j=i-1;j>pre;j--)
                {
                    out+=s[j];
                }
                if (i!=s.size())
                {
                    out+=' ';
                }
                pre=i;
            }
        }
        return out;
    }
};