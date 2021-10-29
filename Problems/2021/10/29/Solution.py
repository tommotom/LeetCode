class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j, 0))

        ans = 0
        while q:
            i, j, time = q.popleft()
            ans = max(ans, time)
            if i > 0 and grid[i-1][j] == 1:
                fresh -= 1
                grid[i-1][j] = 2
                q.append((i-1, j, time+1))
            if j > 0 and grid[i][j-1] == 1:
                fresh -= 1
                grid[i][j-1] = 2
                q.append((i, j-1, time+1))
            if i < len(grid)-1 and grid[i+1][j] == 1:
                fresh -= 1
                grid[i+1][j] = 2
                q.append((i+1, j, time+1))
            if j < len(grid[i])-1 and grid[i][j+1] == 1:
                fresh -= 1
                grid[i][j+1] = 2
                q.append((i, j+1, time+1))

        if fresh > 0: return -1
        return ans
