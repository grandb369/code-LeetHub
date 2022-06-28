class Solution {
public:
    int minDeletions(string s) {
        const int n=s.size();
        vector<int> temp(n+1,0);
        unordered_map<char,int>k;
        for(char i:s)
        {
            k[i]++;
        }
        for(auto &i:k)
        {
            temp[i.second]++;
        }
        int out=0;
        for(int i=s.size()-1;i>=0;i--)
        {
            if(temp[i+1]>1)
            {
                int val=temp[i+1]-1;
                out+=val;
                temp[i]+=val;
            }
        }
        return out;
    }
};