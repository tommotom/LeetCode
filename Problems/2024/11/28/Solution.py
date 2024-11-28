class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        def isValid(r, c):
            return 0 <= r < m and 0 <= c < n

        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        q = [(grid[0][0], 0, 0)]
        visited = set()
        while q:
            step, r, c = heapq.heappop(q)
            if r == m - 1 and c == n - 1: return step
            if ((r, c) in visited): continue
            visited.add((r, c))
            for dr, dc in dirs:
                R, C = r + dr, c + dc
                if not isValid(R, C): continue
                if ((R, C) in visited): continue
                heapq.heappush(q, (step + grid[R][C], R, C))
        return -1
