class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1

        minimum = maximum = nums[0]
        min_i = max_i = 0
        for i in range(1, len(nums)):
            if minimum > nums[i]:
                min_i = i
                minimum = nums[i]
            if maximum < nums[i]:
                max_i = i
                maximum = nums[i]

        l, r = min(min_i, max_i), max(min_i, max_i)

        return min(r+1, len(nums)-l, l+1+(len(nums)-r))
