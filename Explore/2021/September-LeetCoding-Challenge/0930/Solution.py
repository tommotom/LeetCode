class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        subsetSum, remain = divmod(sum(nums), k)
        if max(nums) > subsetSum or remain != 0: return False
        n = len(nums)

        @lru_cache(None)
        def dp(mask):
            if mask == 0: return 0
            for i in range(n):
                if (mask >> i) & 1:
                    newMask = mask ^ (1 << i)
                    remain = dp(newMask)
                    if remain == -1: continue
                    if remain + nums[i] <= subsetSum:
                        return (remain + nums[i]) % subsetSum
            return -1

        return dp((1 << n) - 1) == 0
