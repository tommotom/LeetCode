class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dist = [[inf] * cols for _ in range(rows)]
        dist[0][0] = grid[0][0]
        q = [(dist[0][0], 0, 0)]
        while q:
            d, r, c = heapq.heappop(q)
            if r == rows-1 and c == cols-1:
                return d
            for i, j in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if not 0 <= i < rows or not 0 <= j < cols: continue
                if dist[i][j] <= grid[i][j] + d: continue
                dist[i][j] = d + grid[i][j]
                heapq.heappush(q, (dist[i][j], i, j))

        return dist[-1][-1]
