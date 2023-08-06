class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        thief = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1: thief.append((i, j, 0))

        dirs = ((0,1), (0,-1), (1,0), (-1,0))
        safe = [[None] * n for _ in range(n)]

        while thief:
            i, j, d = thief.popleft()
            if safe[i][j] != None and safe[i][j] <= d: continue
            safe[i][j] = d
            for di in dirs:
                if not 0 <= i + di[0] < n or not 0 <= j + di[1] < n: continue
                thief.append((i+di[0], j+di[1], d+1))

        score = [[None] * n for _ in range(n)]
        q = [(-safe[0][0], 0, 0)]
        while q:
            s, i, j = heapq.heappop(q)
            s *= -1
            s = min(s, safe[i][j])
            if score[i][j] != None and score[i][j] >= s: continue
            score[i][j] = s
            for di in dirs:
                if not 0 <= i + di[0] < n or not 0 <= j + di[1] < n: continue
                heapq.heappush(q, (-s, i+di[0], j+di[1]))

        return score[n-1][n-1]
