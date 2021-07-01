class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        dp = [[0] * (k+1) for _ in range(n)]
        for i in range(len(dp)):
            dp[i][0] = 1
            for j in range(1, min(len(dp[0]), (i+1) * (i+2) // 2 - i)):
                dp[i][j] = (dp[i-1][j] - (dp[i-1][j-i-1] if j-i > 0 else 0) + dp[i][j-1]) % mod
        return dp[-1][-1]
