class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf') for _ in range(len(cost)+1)]
        dp[0] = dp[1] = 0
        for i, c in enumerate(cost):
            dp[i+1] = min(dp[i+1], dp[i]+c)
            if i < len(cost)-1:
                dp[i+2] = min(dp[i+2], dp[i]+c)
        return dp[-1]
