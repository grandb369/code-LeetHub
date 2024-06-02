class Solution {
public:
    void reverseString(vector<char>& s) {
        int n=s.size();
        for(int i=0;i<(int)n/2;i++)
        {
            int temp=s[i];
            s[i]=s[n-1-i];
            s[n-1-i]=temp;
        }
    }
};