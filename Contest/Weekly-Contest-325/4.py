class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 1000000007

        dp = [[0] * (k) for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0] = 1

        for i in range(len(nums)):
            for j in range(k):
                dp[i+1][j] = dp[i][j]
                if j >= nums[i]:
                    dp[i+1][j] += dp[i][j-nums[i]]

        return (max(0, pow(2, len(nums)) - 2*sum(dp[-1]))) % mod
