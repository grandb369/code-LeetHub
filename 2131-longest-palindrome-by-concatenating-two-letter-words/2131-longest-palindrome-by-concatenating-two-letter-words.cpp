class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        map<string,int>temp;
        int count=0;
        int out=0;
        for(string s:words)
        {

            if(temp[s]>0)
            {
                out+=4;
                temp[s]--;
                if(s[0]==s[1])count--;
            }
            else
            {
                reverse(s.begin(),s.end());
                temp[s]++;
                if (s[0]==s[1])count++;
            }
        }
        return count>0?out+2:out;
    }
};