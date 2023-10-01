class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collection = set()
        ope = 0
        while len(collection) < k:
            ope += 1
            if nums[len(nums) - ope] <= k:
                collection.add(nums[len(nums) - ope])
        return ope
