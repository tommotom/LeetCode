class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missing, ans, i = 1, 0, 0
        while missing <= n:
            if i < len(nums) and nums[i] <= missing:
                missing += nums[i]
                i += 1
            else:
                ans += 1
                missing += missing
        return ans
