class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        num_to_i = {}
        for i, num in enumerate(nums):
            num_to_i[num] = i
        for before, after in operations:
            nums[num_to_i[before]] = after
            num_to_i[after] = num_to_i[before]
            del num_to_i[before]
        return nums
