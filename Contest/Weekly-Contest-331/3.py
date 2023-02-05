class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:

        def possible(m):
            dp = [0] * len(nums)
            for i in range(len(nums)):
                if nums[i] <= m:
                    if i > 1:
                        dp[i] = max(dp[i-1], dp[i-2] + 1)
                    else:
                        dp[i] = 1
                else:
                    dp[i] = dp[i-1]

            return dp[-1] >= k

        l, r = min(nums), max(nums)
        while l < r:
            m = l + (r - l) // 2
            if possible(m):
                r = m
            else:
                l = m + 1

        return l
