class Solution {
public:
    int uniquePaths(int m, int n) {
        if(m==1 || n==1)return 1;
        long ans=m+n-2;
        n=min(m,n)-1;
        int upper=ans-1;
        int lower=2;
        for(int i=0;i<n-1;i++)
        {
            ans=ans*upper/lower;
            upper--;
            lower++;
        }
        return ans;
    }
};