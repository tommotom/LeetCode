class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if k % 2 == 1 and len(nums) == 1: return -1
        if k == 1: return nums[1]
        if k == 0: return nums[0]


        ans = max(nums[:min(k-1, len(nums))])
        if k < len(nums):
            ans = max(ans, nums[k])

        return ans
