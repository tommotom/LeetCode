class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])

        def helper(i, j):
            nonlocal ans, count
            if grid[i][j] == 2:
                if count == 0:
                    ans += 1
                return
            if count == 0: return

            grid[i][j] = 3
            count -= 1
            if i > 0 and (grid[i-1][j] == 0 or grid[i-1][j] == 2):
                helper(i-1, j)
            if j > 0 and (grid[i][j-1] == 0 or grid[i][j-1] == 2):
                helper(i, j-1)
            if i+1 < rows and (grid[i+1][j] == 0 or grid[i+1][j] == 2):
                helper(i+1, j)
            if j+1 < cols and (grid[i][j+1] == 0 or grid[i][j+1] == 2):
                helper(i, j+1)
            grid[i][j] = 0
            count += 1


        count = 1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    count += 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    helper(i, j)
                    break
            else:
                continue
            break

        return ans
