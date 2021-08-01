class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        dp = [1,0,0,0]
        for n in nums:
            dp[n+1] += dp[n] + dp[n+1]
        return dp[-1] % (10 ** 9 + 7)
