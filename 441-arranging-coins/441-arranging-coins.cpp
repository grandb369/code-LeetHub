class Solution {
public:
    int arrangeCoins(int n) {
        long l=1;
        long r=n;
        while (l<r)
        {
            long mid=(long)(r-l)/2+l;
            long val=(long)(mid*(mid+1))/2;
            if(val==n)return mid;
            else if(val<n)l=mid+1;
            else r=mid;
        }
        long val=(long)(l*(l+1))/2;
        if(val<=n)return l;
        return l-1;
    }
};