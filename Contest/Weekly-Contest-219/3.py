class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp = [[0] * len(stones) for _ in range(len(stones))]
        cum = [0] + list(accumulate(stones))

        def dfs(i: int, j: int) -> int:
            if i == j: return 0

            if dp[i][j] == 0:
                sum = cum[j+1] - cum[i]
                dp[i][j] = max(sum - stones[i] - dfs(i+1, j), sum - stones[j] - dfs(i, j-1))
            return dp[i][j]

        return dfs(0, len(stones)-1)
