class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        dp = [[0] * (len1+1) for _ in range(len2+1)]
        for i in range(len2):
            for j in range(len1):
                if word1[j] == word2[i]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        return len1+len2 - 2*dp[-1][-1]
