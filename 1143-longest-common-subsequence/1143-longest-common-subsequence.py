class Solution:
    def longestCommonSubsequence(self, text1, text2):
        text1 = "!" + text1
        text2 = "!" + text2
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i, j in product(range(m), range(n)):
            if text1[i] == text2[j]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1] - 1