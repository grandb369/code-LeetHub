class Solution {
public:
    int integerBreak(int n) {
        if(n<4)return n-1;
        int out=1;
        int three=(int)n/3;
        int val=n%3;
        int two=0;
        if (val==1)
        {
            three--;
            two=2;
        }
        else if(val==2)
        {
            two=1;
        }
        out*=(int)pow(3,three);
        out*=(int)pow(2,two);
        return out;
    }
};