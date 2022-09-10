class Solution {
public:
    int maxProfit(int k, vector<int>& nums) {
        if(k==0)return 0;
        vector<int>sell(k,0);
        vector<int>buy(k,-1000);
        for(int v:nums)
        {
            for(int i=k-1;i>=0;i--)
            {
                sell[i]=max(sell[i],buy[i]+v);
                if(i==0)
                {
                    buy[i]=max(buy[i],-v);
                }
                else
                {
                    buy[i]=max(buy[i],sell[i-1]-v);
                }
            }
        }
        
        return max(0,sell[k-1]);
    }
};