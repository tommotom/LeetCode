class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        if target == 0: return 0
        total = sum(nums)
        if total < target:
            tmp = self.minSizeSubarray(nums, target % total)
            if tmp == -1: return tmp
            return tmp + len(nums) * (target // total)

        nums = nums + nums
        cur = 0
        ans = float('inf')
        l = -1
        for r in range(len(nums)):
            cur += nums[r]
            while l < r and cur > target:
                l += 1
                cur -= nums[l]
            if cur == target:
                ans = min(ans, r - l)

        return -1 if ans == float('inf') else ans
