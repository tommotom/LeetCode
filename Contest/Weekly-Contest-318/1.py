class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0

        zeros, remain = [], []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros.append(0)
            else:
                remain.append(nums[i])

        return remain + zeros
