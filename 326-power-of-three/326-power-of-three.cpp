class Solution {
public:
    bool isPowerOfThree(int n) {
        if (n<=0)return false;
        int v=1162261467;
        return v%n==0;
    }
};