class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf") for _ in range(n)]
        dp[0] = 0
        for i in range(n-1):
            for jump in range(1, nums[i]+1):
                if i+jump >= n: break
                dp[i+jump] = min(dp[i+jump], dp[i]+1)
        return dp[-1]
