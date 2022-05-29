class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        dp = [0] * n
        ans = 0
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i] + 1, dp[stack.pop()])
            ans = max(ans, dp[i])
            stack.append(i)
        return ans
