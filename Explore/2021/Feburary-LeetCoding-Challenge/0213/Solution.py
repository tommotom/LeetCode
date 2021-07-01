from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1: return -1
        rows, cols = len(grid), len(grid[0])
        q = deque([(0,0,1)])
        visited = set()
        while q:
            r, c, length = q.popleft()
            if r == rows-1 and c == cols-1: return length
            if (r, c) in visited: continue
            visited.add((r,c))
            if r > 0 and (r-1, c) not in visited and grid[r-1][c] == 0: q.append((r-1, c, length+1))
            if r > 0 and c < cols - 1 and (r-1, c+1) not in visited and grid[r-1][c+1] == 0: q.append((r-1, c+1, length+1))
            if c < cols - 1 and (r, c+1) not in visited and grid[r][c+1] == 0: q.append((r, c+1, length+1))
            if r < rows - 1 and c < cols - 1 and (r+1, c+1) not in visited and grid[r+1][c+1] == 0: q.append((r+1, c+1, length+1))
            if r < rows - 1 and (r+1, c) not in visited and grid[r+1][c] == 0: q.append((r+1, c, length+1))
            if r < rows - 1 and c > 0 and (r+1, c-1) not in visited and grid[r+1][c-1] == 0: q.append((r+1, c-1, length+1))
            if c > 0 and (r, c-1) not in visited and grid[r][c-1] == 0: q.append((r, c-1, length+1))
            if r > 0 and c > 0 and (r-1, c-1) not in visited and grid[r-1][c-1] == 0: q.append((r-1, c-1, length+1))
        return -1
