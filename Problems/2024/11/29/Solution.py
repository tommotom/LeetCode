class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[1][0] > 1 and grid[0][1] > 1: return -1

        m, n = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        arrived = [[float('inf')] * n for _ in range(m)]
        arrived[0][0] = 0
        q = [(0,0,0)]
        while True:
            t, r, c = heapq.heappop(q)
            if r == m-1 and c == n-1: return t
            for d in dirs:
                next_r = r + d[0]
                next_c = c + d[1]
                if not 0 <= next_r < m: continue
                if not 0 <= next_c < n: continue
                if arrived[next_r][next_c] != float('inf'): continue
                if t+1 >= grid[next_r][next_c]:
                    arrived[next_r][next_c] = t+1
                else:
                    time = ((grid[next_r][next_c] - t) // 2) * 2 + 1
                    arrived[next_r][next_c] = t + time
                heapq.heappush(q, (arrived[next_r][next_c], next_r, next_c))
