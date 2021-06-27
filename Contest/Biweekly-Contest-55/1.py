class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        def strictryIncreasing(nums):
            for i in range(len(nums)-1):
                if not nums[i] < nums[i+1]:
                    return False
            return True

        for i in range(len(nums)):
            if strictryIncreasing(nums[:i] + nums[i+1:]):
                return True
        return False
