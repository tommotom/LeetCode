class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if len(nums) == 1: return True

        def isValid(i, j):
            return i+1 == j or sum(nums[i:j]) >= m

        @lru_cache(None)
        def helper(i, j):
            if i+1 == j: return True
            for k in range(i+1, j):
                if isValid(i, k) and isValid(k, j) and helper(i, k) and helper(k, j):
                    return True
            return False

        return helper(0, len(nums))
