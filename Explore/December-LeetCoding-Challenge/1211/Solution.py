class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while True:
            while i+2 < len(nums) and nums[i] == nums[i+2]: nums.pop(i)
            if i+2 >= len(nums): break
            i += 1
        return
