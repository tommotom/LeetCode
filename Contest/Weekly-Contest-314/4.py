class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        mod = 1000000007

        dp = [[[0] * k for _ in range(n)] for __ in range(m)]
        dp[0][0][grid[0][0]%k] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                num = grid[i][j]
                for l in range(k):
                    if i > 0:
                        index = (l - num + 100 * k) % k
                        dp[i][j][l] += dp[i-1][j][index]
                        dp[i][j][l] %= mod
                    if j > 0:
                        index = (l - num + 100 * k) % k
                        dp[i][j][l] += dp[i][j-1][index]
                        dp[i][j][l] %= mod

        return dp[-1][-1][0]
