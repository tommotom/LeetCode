class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length, containsOne = len(nums), False
        for i in range(length):
            if nums[i] == 1: containsOne = True
            if nums[i] < 1 or nums[i] > length: nums[i] = 1

        if not containsOne: return 1

        for i in range(length):
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1

        for i in range(length):
            if nums[i] > 0: return i+1

        return length + 1
