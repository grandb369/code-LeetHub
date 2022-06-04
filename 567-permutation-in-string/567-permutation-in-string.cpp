class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        vector<int>k1(26);
        vector<int>k2(26);
        if (s1.size()>s2.size())return false;
        for(char s:s1)
        {
            k1[s-'a']++;
        }
        for(int i=0;i<s1.size();i++)
        {
            k2[s2[i]-'a']++;
        }
        if(k1==k2)return true;
        int n=s1.size();
        for(int i=n;i<s2.size();i++)
        {
            k2[s2[i-n]-'a']--;
            k2[s2[i]-'a']++;
            if(k1==k2)return true;
        }
        return false;
    }
};