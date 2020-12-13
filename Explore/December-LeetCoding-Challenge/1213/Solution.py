class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [[0] * len(nums) for _ in range(len(nums))]
        i = j = 0
        while j < len(nums):
            i = 0
            while j < len(nums):
                for k in range(i, j+1):
                    point = nums[k]
                    if i > 0: point *= nums[i-1]
                    if j + 1 < len(nums): point *= nums[j+1]
                    if k > i: point += dp[i][k-1]
                    if k < j: point += dp[k+1][j]
                    dp[i][j] = max(dp[i][j], point)
                i += 1; j += 1
            j -= i - 1
        return dp[0][len(nums)-1]
