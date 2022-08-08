class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [[0] * 26 for _ in range(len(s))]
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            if i == 0:
                dp[i][index] += 1
                continue

            for j in range(26):
                dp[i][j] = dp[i-1][j]

            for j in range(max(0, index-k), min(26, index+k+1)):
                dp[i][index] = max(dp[i][index], dp[i-1][j])
            dp[i][index] += 1

        return max(dp[len(s)-1])
