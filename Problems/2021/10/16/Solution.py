class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        left_to_right = [0] * n
        right_to_left = [0] * n

        minimum = prices[0]
        for i in range(n):
            left_to_right[i] = max(left_to_right[i-1], prices[i] - minimum)
            minimum = min(minimum, prices[i])

        maximum = prices[-1]
        for i in range(n-2, -1, -1):
            right_to_left[i] = max(right_to_left[i+1], maximum - prices[i])
            maximum = max(maximum, prices[i])

        ans = max(left_to_right[-1], right_to_left[0])
        for i in range(n-1):
            ans = max(ans, left_to_right[i] + right_to_left[i+1])

        return ans
