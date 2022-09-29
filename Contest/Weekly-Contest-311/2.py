class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        dp = [0] * len(s)
        for i, c in enumerate(s):
            if i > 0 and ord(s[i-1]) + 1 == ord(s[i]):
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = 1
        return max(dp)
