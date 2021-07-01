class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        dp = [[[-1] * col for c in range(col)] for r in range(row)]

        def helper(idx, j1, j2):
            nonlocal grid

            if idx == row: return 0
            if not (0 <= j1 < col) or not (0 <= j2 < col): return -float('inf')
            if not dp[idx][j1][j2] == -1: return dp[idx][j1][j2]

            cur = grid[idx][j1] + grid[idx][j2]
            if j1 == j2: cur -= grid[idx][j1]

            ans = -float('inf')
            ans = max(ans, cur + helper(idx+1, j1-1, j2-1))
            ans = max(ans, cur + helper(idx+1, j1, j2-1))
            ans = max(ans, cur + helper(idx+1, j1+1, j2-1))
            ans = max(ans, cur + helper(idx+1, j1-1, j2))
            ans = max(ans, cur + helper(idx+1, j1, j2))
            ans = max(ans, cur + helper(idx+1, j1+1, j2))
            ans = max(ans, cur + helper(idx+1, j1-1, j2+1))
            ans = max(ans, cur + helper(idx+1, j1, j2+1))
            ans = max(ans, cur + helper(idx+1, j1+1, j2+1))

            dp[idx][j1][j2] = ans
            return ans

        return helper(0, 0, col-1)
