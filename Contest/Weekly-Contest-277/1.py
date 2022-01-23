class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        while l < len(nums) and nums[0] == nums[l]:
            l += 1
        r = len(nums)-1
        while r > 0 and nums[-1] == nums[r]:
            r -= 1

        return max(r-l+1, 0)
