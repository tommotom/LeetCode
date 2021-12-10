class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [1, 2, 5] + [0] * n
        for i in range(3, n):
            dp[i] = (dp[i-1] * 2 + dp[i-3]) % mod
        return dp[n-1]
