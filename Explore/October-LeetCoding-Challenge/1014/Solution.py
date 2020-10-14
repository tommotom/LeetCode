class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2: return nums[0]

        dp = [0] * (len(nums) + 1)
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
        tmp = dp[-1]

        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i-1])

        return max(tmp, dp[-1])
