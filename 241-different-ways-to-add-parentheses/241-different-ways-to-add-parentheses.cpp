#include <string>
class Solution {
public:
    vector<int> cal(string s)
    {
        vector<int>out,left,right;
        int count=0;
        for(int i=0;i<s.size();i++)
        {
            if (s[i]=='+' || s[i]=='-' || s[i]=='*')
            {
                count++;
                string ls=s.substr(0,i);
                string rs=s.substr(i+1);
                left=cal(ls);
                right=cal(rs);
                for(int l:left)
                {
                    for(int r:right)
                    {
                        if(s[i]=='-')out.push_back(l-r);
                        else if(s[i]=='+')out.push_back(l+r);
                        else out.push_back(l*r);
                    }
                }
            }
        }
        if(count==0)
        {
            out.push_back(stoi(s));
        }
        return out;
    }
    
    vector<int> diffWaysToCompute(string s) {
        vector<int>out=cal(s);
        return out;
        
    }
};