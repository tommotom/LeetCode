class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        points = defaultdict(int)
        for num in nums:
            points[num] += num

        @cache
        def helper(num):
            nonlocal points
            if num < 1: return 0

            return max(points[num] + helper(num-2), helper(num-1))

        return helper(max(nums))
