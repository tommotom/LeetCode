class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l+1 < r:
            m = (l + r) // 2
            if nums[m] > nums[m+1]: return nums[m+1]
            if nums[l] > nums[m]: r = m
            elif nums[m] > nums[r]: l = m
            else: return nums[l]
        return min(nums)
