class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            rest = target - num
            if rest in num_to_idx:
                return [num_to_idx[rest], i]
            num_to_idx[num] = i
        return []
