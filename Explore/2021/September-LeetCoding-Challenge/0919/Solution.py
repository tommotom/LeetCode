class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * len(s) for _ in range(len(t))]
        for i in range(len(t)):
            for j in range(i,len(s)):
                if j > 0:
                    dp[i][j] = dp[i][j-1]
                if t[i] == s[j]:
                    dp[i][j] += dp[i-1][j-1] if i > 0 and j > 0 else 1
        return dp[-1][-1]
