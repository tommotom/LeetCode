class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        arr = [1] + nums + [1]

        dp = [[0] * (n+2) for _ in range(n+2)]
        for window in range(1, n+1):
            for left in range(1, n - window + 2):
                right = left + window - 1
                for i in range(left, right + 1):
                    dp[left][right] = max(dp[left][right], arr[left-1] * arr[i] * arr[right+1] + dp[left][i-1] + dp[i+1][right])
        return dp[1][n]
