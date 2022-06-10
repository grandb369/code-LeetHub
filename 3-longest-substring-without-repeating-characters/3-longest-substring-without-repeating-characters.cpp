class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char>temp;
        int pre=0;
        int out=0;
        for(int i=0;i<s.size();i++)
        {
            if(temp.find(s[i])==temp.end())
            {
                temp.insert(s[i]);
            }
            else
            {
                int n=temp.size();
                out=max(out,n);
                while(s[pre]!=s[i])
                {
                    temp.erase(s[pre]);
                    pre++;
                }
                temp.erase(s[pre]);
                pre++;
                temp.insert(s[i]);
            }
        }
        int n=temp.size();
        return max(out,n);
    }
};