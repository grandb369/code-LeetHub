class Solution {
public:
    bool halvesAreAlike(string s) {
        string ss="aeiouAEIOU";
        int count=0;
        for(int i=0;i<s.size();i++)
        {
            bool ans=false;
            for(char c:ss)
            {
                if(c==s[i])
                {
                    ans=true;
                    break;
                }
            }
            if(ans)
            {
                if(i<s.size()/2)count++;
                else count--;
            }
        }
        return count==0;
    }
};