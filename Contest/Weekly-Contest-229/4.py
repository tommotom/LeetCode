class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        m, n, ans = len(word1), len(word2), 0
        dp = [[0] * (m+n) for _ in range(m+n)]
        for j in range(m+n):
            dp[j][j] = 1
            for i in range(j-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = 2 if i+1 == j else dp[i+1][j-1] + 2
                    if i < m <= j: ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return ans