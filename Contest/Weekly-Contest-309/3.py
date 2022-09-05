class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l, r, cur, ans = 0, 1, nums[0], 1
        while l < len(nums):
            if r < len(nums) and cur & nums[r] == 0:
                cur |= nums[r]
                r += 1
                ans = max(ans, r-l)
            else:
                cur ^= nums[l]
                l += 1
        return ans
