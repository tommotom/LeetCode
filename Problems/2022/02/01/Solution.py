class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            ans = max(ans, prices[i]-minimum)
            minimum = min(minimum, prices[i])
        return ans
