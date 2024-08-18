class Solution {
public:
    int nthUglyNumber(int n) {
        int tw=0,th=0,fi=0;
        vector<int>dp{1};
        int v1,v2,v3;
        while(dp.size()<n)
        {
            v1=dp[tw]*2;
            v2=dp[th]*3;
            v3=dp[fi]*5;
            int val=min(v1,min(v2,v3));
            if(v1==val)tw++;
            if(v2==val)th++;
            if(v3==val)fi++;
            dp.push_back(val);
        }
        return dp[n-1];
    }
};