class Solution {
public:
    int consecutiveNumbersSum(int n) {
        int out=0;
        int val=(int)(sqrt(2*n+0.25)-0.5)+1;
        for(int k=1;k<val;k++)
        {
            int val = n-(int)(k*(k+1)/2);
            if(val%k==0)out++;
        }
        return out;
    }
};