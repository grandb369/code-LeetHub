class Solution {
public:
    string longestPalindrome(string s) {
        int out=0;
        string ans="";
        int n=s.size();
        for (int i=0;i<n;i++)
        {
            int l=i;
            int r=i;
            while (l-1>=0 && r+1<n && s[l-1]==s[r+1])
            {
                l--;
                r++;
            }
            if (out<r-l+1)
            {
                out=r-l+1;
                ans=s.substr(l,r-l+1);
            }
            if(i-1>=0 && s[i-1]==s[i])
            {
                l=i-1;
                r=i;
                while (l-1>=0 && r+1<n && s[l-1]==s[r+1])
                {
                    l--;
                    r++;
                }
                if (out<r-l+1)
                {
                    out=r-l+1;
                    ans=s.substr(l,r-l+1);
                }
            }
        }
        return ans;
    }
};