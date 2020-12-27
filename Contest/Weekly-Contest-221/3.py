class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        row, col = len(grid), len(grid[0])
        ans = []

        def isVShape(i, j):
            if grid[i][j] == 1:
                return j + 1 == col or grid[i][j+1] == -1
            else:
                return j == 0 or grid[i][j-1] == 1

        for c in range(col):
            j = c
            for i in range(row):
                if isVShape(i, j):
                    ans.append(-1)
                    break

                if grid[i][j] == 1:
                    j += 1
                else:
                    j -= 1
            else:
                ans.append(j)
        return ans
