class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n)]
        for j in range(5):
            dp[0][j] = 1
        for i in range(1, n):
            cum = 0
            for j in range(5):
                cum += dp[i-1][j]
                dp[i][j] = cum
        return sum(dp[-1])
