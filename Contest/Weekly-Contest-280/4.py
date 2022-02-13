class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        @lru_cache(None)
        def dp(i, mask):
            res = 0
            if i == len(nums): return 0
            for slot in range(1, numSlots+1):
                b = pow(3, slot-1)
                if mask // b % 3 > 0:
                    res = max(res, (nums[i] & slot) + dp(i+1, mask - b))
            return res

        return dp(0, pow(3, numSlots)-1)
