class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i):
            if i == len(nums): return True
            if i+1 < len(nums) and nums[i] == nums[i+1] and dfs(i+2): return True
            if i+2 < len(nums) and nums[i] == nums[i+1] == nums[i+2] and dfs(i+3): return True
            if i+2 < len(nums) and nums[i] + 2 == nums[i+1] + 1 == nums[i+2] and dfs(i+3): return True
            return False

        return dfs(0)
