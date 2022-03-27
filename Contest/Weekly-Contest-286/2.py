class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        deleted = 0
        for i in range(len(nums)-1):
            if (i-deleted) % 2 == 0 and nums[i] == nums[i+1]:
                deleted += 1
        if (len(nums) - deleted) % 2 == 1:
            deleted += 1
        return deleted
