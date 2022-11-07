class Solution {
public:
    int maximum69Number (int num) {
        int count=1;
        int out=0;
        int temp=0;
        while(num>0)
        {
            temp*=10;
            temp+=num%10;
            num/=10;
        }
        while(temp>0)
        {
            out*=10;
            int cur=temp%10;
            if(cur==6 && count==1)
            {
                out+=9;
                count--;
            }
            else
            {
                out+=cur;
            }
            temp/=10;
        }
        return out;
    }
};