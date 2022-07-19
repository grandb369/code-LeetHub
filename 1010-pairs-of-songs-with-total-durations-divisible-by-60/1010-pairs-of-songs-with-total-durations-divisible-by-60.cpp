class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        map<int,int,greater<int>>temp;
        for(int t:time)
        {
            temp[t%60]++;
        }
        long out=(long)((long)temp[0]*(temp[0]-1)/2);
        for(auto it:temp)
        {
            if(it.first==30)
            {
                out+=(long)((long)it.second*(it.second-1)/2);
            }
            else if(it.first>30)out+=(long)it.second*temp[60-it.first];
            
        }
        return out;
    }
};