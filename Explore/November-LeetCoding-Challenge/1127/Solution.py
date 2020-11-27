class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot % 2 == 1: return False
        target = tot // 2
        dp = [[0] * (target+1) for _ in range(len(nums))]

        for j in range(nums[0], target+1): dp[0][j] = nums[0]

        for i in range(len(dp)):
            for j in range(target+1):
                if nums[i] <= j:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-nums[i]] + nums[i])
                else: dp[i][j] = dp[i-1][j]

        return dp[-1][-1] == target
