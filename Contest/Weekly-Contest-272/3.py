class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        dp = [1 for _ in range(len(prices))]
        for i in range(1, len(prices)):
            if prices[i-1] -1 == prices[i]:
                dp[i] += dp[i-1]
        return sum(dp)
