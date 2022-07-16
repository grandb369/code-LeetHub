class Solution {
public:
    int longestValidParentheses(string s) {
        int n=s.size();
        int l=0;
        int r=0;
        int out=0;
        for(char i:s)
        {
            if(i=='(')
            {
                l+=1;
            }
            else r+=1;
            if(l==r)out=max(out,l*2);
            if(r>l)l=r=0;
        }
        l=r=0;
        for(int i=n-1;i>=0;i--)
        {
            if(s[i]==')')
            {
                r+=1;
            }
            else l+=1;
            if(l==r)out=max(out,r*2);
            if(l>r)l=r=0;
        }
        return out;
    }
};