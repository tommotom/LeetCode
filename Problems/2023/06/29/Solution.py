class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        m, n = len(grid), len(grid[0])
        keys = 0
        start = None
        for i in range(m):
            for j in range(n):
                if grid[i][j].islower(): keys += 1
                if grid[i][j] == '@': start = (i, j)

        dp = [[[float('inf')] * pow(2, keys) for _ in range(n)] for _ in range(m)]

        q = [(0, 0, start[0], start[1])]

        while q:
            step, key, row, col = heapq.heappop(q)
            if key == pow(2, keys) - 1: return step
            if dp[row][col][key] <= step: continue

            dp[row][col][key] = step

            if grid[row][col].islower():
                k = ord(grid[row][col]) - ord('a')
                if key & (1 << k) == 0:
                    key |= (1 << k)
                    heapq.heappush(q, (step, key, row, col))
                    continue

            for i, j in dirs:
                if not (0 <= row+i < m and 0 <= col+j < n): continue
                if grid[row+i][col+j] == "#": continue
                if grid[row+i][col+j].isupper():
                    k = ord(grid[row+i][col+j]) - ord('A')
                    if key & (1 << k) == 0: continue
                heapq.heappush(q, (step+1, key, row+i, col+j))

        return -1
