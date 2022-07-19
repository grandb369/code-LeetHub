class Solution {
public:
    int numTeams(vector<int>& v) {
        int n = v.size(), ans = 0;
        vector dp(n, vector<int>(3)), dp2(n, vector<int>(3));
        for (int i = 0; i < n; ++i) {
            dp[i][0] = dp2[i][0] = 1;
            for (int j = 0; j < i; ++j) {
                if (v[j] < v[i]) {
                    dp[i][1] += dp[j][0];
                    dp[i][2] += dp[j][1];
                } else {
                    dp2[i][1] += dp2[j][0];
                    dp2[i][2] += dp2[j][1];
                }
            }
            ans += dp[i][2] + dp2[i][2];
        }
        return ans;
    }
};