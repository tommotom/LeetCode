class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        cum1, cum2 = [grid[0][0]], [grid[1][0]]
        for i in range(1, len(grid[0])):
            cum1.append(cum1[-1] + grid[0][i])
            cum2.append(cum2[-1] + grid[1][i])

        ans = float('inf')
        for i in range(len(grid[0])):
            tmp = cum1[-1] - cum1[i]
            if i > 0:
                tmp = max(tmp, cum2[i-1])
            ans = min(ans, tmp)
        return ans
