class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        minimum = cur = 0
        ans = -float('inf')
        for num in nums:
            minimum = min(minimum, cur)
            cur += num
            ans = max(ans, cur - minimum)
        return ans
