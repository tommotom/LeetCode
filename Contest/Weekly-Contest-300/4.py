class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10**9 + 7

        @lru_cache(None)
        def dfs(i, j):
            nonlocal m, n, mod
            res = 1
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n:
                    if grid[x][y] < grid[i][j]:
                        res = (res + dfs(x, y)) % mod
            return res

        return sum(sum(dfs(i, j) for j in range(n)) for i in range(m)) % mod
