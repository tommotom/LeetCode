class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal grid, rows, cols
            grid[i][j] = 2
            ret = 1
            if i > 0 and grid[i-1][j] == 1:
                ret += dfs(i-1, j)
            if j > 0 and grid[i][j-1] == 1:
                ret += dfs(i, j-1)
            if i + 1 < rows and grid[i+1][j] == 1:
                ret += dfs(i+1, j)
            if j + 1 < cols and grid[i][j+1] == 1:
                ret += dfs(i, j+1)
            return ret

        rows, cols = len(grid), len(grid[0])
        ans = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
