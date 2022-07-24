class Solution {
public:
    vector<string> generatePossibleNextMoves(string s) {
        int n=s.size();
        vector<string>out;
        for (int i=0;i<n-1;i++)
        {
            if(s[i]=='+' && s[i+1]=='+')
            {
                s[i]=s[i+1]='-';
                out.push_back(s);
                s[i]=s[i+1]='+';
            }
            
        }
        return out;
    }
};