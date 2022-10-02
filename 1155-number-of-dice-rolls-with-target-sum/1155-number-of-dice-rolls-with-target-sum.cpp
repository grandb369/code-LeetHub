class Solution {
public:
    int numRollsToTarget(int n, int k, int target) {
        int mod=1000000007;
        vector<int>dp(target+1,0);
        for(int i=1;i<=k;i++)
        {
            if(i<target+1)
            {
                dp[i]=1;
            }
            else break;
        }
        for(int i=0;i<n-1;i++)
        {
            vector<int>nex(target+1,0);
            for(int x=1;x<target+1;x++)
            {
                if(dp[x]!=0)
                {
                    for(int y=1;y<=k;y++)
                    {
                        if(x+y>=target+1)
                        {
                            break;
                        }
                        nex[x+y]+=dp[x];
                        nex[x+y]%=mod;
                    }
                }
            }
            dp=nex;
        }
        return dp[target];
    }
};