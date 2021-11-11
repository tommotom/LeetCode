class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum = float('inf')
        val = 0
        for num in nums:
            val += num
            minimum = min(minimum, val)

        return - minimum + 1 if minimum < 0 else 1
