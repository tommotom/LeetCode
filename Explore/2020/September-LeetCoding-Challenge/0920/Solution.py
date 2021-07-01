class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ans = 0

        def backtrack(zeros, r, c):
            nonlocal ans
            if zeros == 0:
                if r > 0 and grid[r-1][c] == 2: ans += 1
                if r < rows - 1 and grid[r+1][c] == 2: ans += 1
                if c > 0 and grid[r][c-1] == 2: ans += 1
                if c < cols - 1 and grid[r][c+1] == 2: ans += 1
                return

            grid[r][c] = 3
            if r > 0 and grid[r-1][c] == 0: backtrack(zeros-1, r-1, c)
            if r < rows - 1 and grid[r+1][c] == 0: backtrack(zeros-1, r+1, c)
            if c > 0 and grid[r][c-1] == 0: backtrack(zeros-1, r, c-1)
            if c < cols - 1 and grid[r][c+1] == 0: backtrack(zeros-1, r, c+1)
            grid[r][c] = 0

            return

        count, x, y = 0, 0, 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    count += 1
                elif grid[i][j] == 1:
                    x, y = i, j

        backtrack(count, x, y)
        return ans
