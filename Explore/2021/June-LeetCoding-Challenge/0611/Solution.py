class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        cum = [0] * n
        cum[0] = stones[0]
        for i in range(1, len(stones)):
            cum[i] = cum[i-1] + stones[i]

        dp = [[[0,0]] * n for _ in range(n)]

        for s in range(1, n):
            for l in range(n-s):
                r = s + l
                pat1 = dp[l+1][r][1] + cum[r] - cum[l]
                pat2 = dp[l][r-1][1] + cum[r-1] - (cum[l-1] if l > 0 else 0)
                if pat1 - dp[l+1][r][0] > pat2 - dp[l][r-1][0]:
                    dp[l][r] = [pat1, dp[l+1][r][0]]
                else:
                    dp[l][r] = [pat2, dp[l][r-1][0]]
        return dp[0][n-1][0] - dp[0][n-1][1]
