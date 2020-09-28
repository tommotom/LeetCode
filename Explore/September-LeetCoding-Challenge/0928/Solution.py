class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i, cum, ans = 0, 1, 0
        for j in range(len(nums)):
            cum *= nums[j]
            while i < j and cum >= k:
                cum //= nums[i]
                i += 1
            ans += j - i
            if cum < k: ans += 1
        return ans
