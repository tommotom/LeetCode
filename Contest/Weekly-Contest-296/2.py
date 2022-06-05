class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        m = M = nums[0]
        ans = 1
        for i in range(1, len(nums)):
            if max(M, nums[i]) - min(m, nums[i]) > k:
                ans += 1
                m = M = nums[i]
            else:
                m = min(m, nums[i])
                M = max(M, nums[i])
        return ans
