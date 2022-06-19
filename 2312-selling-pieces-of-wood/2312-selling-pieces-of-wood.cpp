class Solution {
public:
    long long sellingWood(int m, int n, vector<vector<int>>& prices) {
        vector dp(m+1, vector(n+1, 0LL));
        for (auto e : prices) {
            dp[e[0]][e[1]] = e[2];
        }
        for (int i = 1; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                for (int x = 1; x < i; ++x) {
                    dp[i][j] = max(dp[i][j], dp[x][j] + dp[i-x][j]);
                }
                for (int x = 1; x < j; ++x) {
                    dp[i][j] = max(dp[i][j], dp[i][x] + dp[i][j-x]);
                }
            }
        }
        return dp[m][n];
    }
};