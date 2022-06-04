class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int pre=0;
        int out=0;
        set<char>temp;
        for(int i=0;i<s.size();i++)
        {
            if(temp.find(s[i])!=temp.end())
            {
                int val=temp.size();
                out=max(out,val);
                while (s[pre]!=s[i])
                {
                    temp.erase(s[pre]);
                    pre++;
                }
                pre++;
            }
            else temp.insert(s[i]);
        }
        int val=temp.size();
        return max(out,val);
    }
};