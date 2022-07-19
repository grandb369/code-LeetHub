class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int k=(int)sqrt(2*n+0.25)-0.5+1;
        int out=0;
        for(int i=1;i<=k;i++)
        {
            int val=n-(int)(i*(i+1)/2);
            if(val%i==0)out++;
        }
        return out;
    }
};