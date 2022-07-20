class Solution {
public:
    int consecutiveNumbersSum(int n) {
        //n=x+1+x+2+..x+k
        //n=xk+(k+1)*k/2
        
        //n/k-(k+1)/2=x>=0
        
        //n/k>=(k+1)/2
        //2n>=k**2+k+1/4-1/4
        //2n+1/4>=(k+1/2)**2
        //k<=(2n+1/4)**0.5-0.5
        int out=0;
        int v=(int)(sqrt(2*n+0.25)+0.5);
        for(int k=1;k<v;k++)
        {
            int val=n-(int)((k+1)*k/2);
            if(val%k==0)out++;
        }
        return out;
    }
};