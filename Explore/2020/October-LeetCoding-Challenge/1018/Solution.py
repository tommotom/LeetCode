class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k > n/2: return self.helper(prices)

        dp = [[0] * n for _ in range(k+1)]
        for i in range(1, k+1):
            diff = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + diff)
                diff = max(diff, dp[i-1][j] - prices[j])
        return dp[-1][-1]

    def helper(self, prices):
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] - prices[i-1] > 0: ans += prices[i] - prices[i-1]
        return ans
