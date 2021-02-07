class Solution:
    def check(self, nums: List[int]) -> bool:
        target = min(nums)
        for min_idx in [i for i, x in enumerate(nums) if x == target]:
            for i in range(min_idx + 1, len(nums)):
                if nums[i-1] > nums[i]: break
            else:
                for i in range(0, min_idx):
                    if nums[i-1] > nums[i]: break
                else: return True
        return False
