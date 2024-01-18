class Solution {
public:
    int climbStairs(int n) {
        if (n==1)return 1;
        if (n==2)return 2;
        int cur=2;
        int pre=1;
        for (int i=3;i<n+1;i++)
        {
            int nex=cur+pre;
            pre=cur;
            cur=nex;
        }
        return cur;
    }
};