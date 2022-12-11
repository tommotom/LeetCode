class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            grid[i].sort()

        for j in range(len(grid[0])):
            tmp = 0
            for i in range(len(grid)):
                tmp = max(tmp, grid[i][j])
            ans += tmp

        return ans
