class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        min_val = min(nums)
        nums.sort()

        @lru_cache(maxsize=None)
        def helper(n):
            nonlocal nums

            if n == 0: return 1
            if n < min_val: return 0

            ans = 0
            for num in nums:
                if num > n: break
                ans += helper(n - num)
            return ans

        return helper(target)
