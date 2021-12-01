class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if i > 2:
                dp[i] = max(dp[i-2], dp[i-3])
            elif i > 1:
                dp[i] = dp[i-2]
            dp[i] += nums[i]
        return max(dp)
