class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        a = b = (0, -1)
        for i in range(n):
            q = []
            for j in range(n):
                if a[1] != j: heapq.heappush(q, (a[0] + grid[i][j], j))
                if b[1] != j: heapq.heappush(q, (b[0] + grid[i][j], j))
            a = b = heapq.heappop(q)
            while a[1] == b[1] and q: b = heapq.heappop(q)

        return a[0]
