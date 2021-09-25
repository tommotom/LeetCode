class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque([(0, 0, k, 0)])
        visited = {(0, 0): k}

        def visit(r, c, obst, cost):
            nonlocal grid, rows, cols, q, visited
            if r < 0 or c < 0 or r >= rows or c >= cols: return
            if (r, c) in visited and obst <= visited[(r, c)]: return

            if grid[r][c] == 0:
                q.append((r, c, obst, cost+1))
                visited[(r, c)] = obst
            elif grid[r][c] == 1 and obst > 0:
                q.append((r, c, obst-1, cost+1))
                visited[(r, c)] = obst-1

        while q:
            r, c, obst, cost = q.popleft()
            if r == rows - 1 and c == cols - 1: return cost
            visit(r-1, c, obst, cost)
            visit(r+1, c, obst, cost)
            visit(r, c-1, obst, cost)
            visit(r, c+1, obst, cost)

        return -1
