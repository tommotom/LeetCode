class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        ans, minimum = 0, prices[0]
        for i in range(1,len(prices)):
            ans = max(ans, prices[i] - minimum)
            minimum = min(minimum, prices[i])
        return ans
