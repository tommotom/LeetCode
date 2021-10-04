class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0: continue
                if i == 0 or grid[i-1][j] == 0: ans += 1
                if j == 0 or grid[i][j-1] == 0: ans += 1
                if i == row-1 or grid[i+1][j] == 0: ans += 1
                if j == col-1 or grid[i][j+1] == 0: ans += 1
        return ans
