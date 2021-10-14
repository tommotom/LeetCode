class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        num = 1
        while num ** 2 <= n:
            sq = num ** 2
            for i in range(sq, n+1):
                dp[i] = min(dp[i], dp[i-sq]+1)
            num += 1
        return dp[-1]
