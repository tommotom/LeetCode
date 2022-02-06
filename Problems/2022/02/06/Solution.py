class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 2, 2
        while i < len(nums) and j < len(nums):
            nums[i] = nums[j]
            if nums[i-2] == nums[i-1] == nums[i]:
                while j < len(nums) and nums[i] == nums[j]:
                    j += 1
                if j == len(nums): break
            else:
                i += 1
                j += 1
        return i
