class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        diff = -prices[0]
        minimum = prices[0]
        for i in range(1, n):
            dp[i] = max(dp[i-1], prices[i] + diff, prices[i] - minimum)
            minimum = min(minimum, prices[i])
            if i > 1:
                diff = max(diff, dp[i-2] - prices[i])
        return dp[-1]
