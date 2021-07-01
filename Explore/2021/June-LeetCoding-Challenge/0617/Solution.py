class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        lastOver = -1
        for i in range(n):
            if right < nums[i]:
                lastOver = i
            else:
                if left <= nums[i]:
                    dp[i] += i - lastOver
                elif i > 0:
                    dp[i] += dp[i-1]
        return sum(dp)
