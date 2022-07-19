class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        map<int,int,greater<int>>temp;
        int out=0;
        for(int t:time)
        {
            out+=temp[60-t%60==60?0:60-t%60];
            temp[t%60]++;
        }
        return out;
    }
};