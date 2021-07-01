class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        med = int(statistics.median(nums))
        ans = 0
        for num in nums:
            ans += abs(med - num)
        return ans
