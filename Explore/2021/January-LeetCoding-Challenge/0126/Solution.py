from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        q = deque([(0,0)])
        while q:
            i, j = q.popleft()
            if i > 0:
                effort = abs(heights[i-1][j] - heights[i][j])
                if efforts[i-1][j] > max(efforts[i][j], effort):
                    efforts[i-1][j] = max(efforts[i][j], effort)
                    q.append((i-1, j))
            if j > 0:
                effort = abs(heights[i][j-1] - heights[i][j])
                if efforts[i][j-1] > max(efforts[i][j], effort):
                    efforts[i][j-1] = max(efforts[i][j], effort)
                    q.append((i, j-1))
            if i < rows - 1:
                effort = abs(heights[i+1][j] - heights[i][j])
                if efforts[i+1][j] > max(efforts[i][j], effort):
                    efforts[i+1][j] = max(efforts[i][j], effort)
                    q.append((i+1, j))
            if j < cols - 1:
                effort = abs(heights[i][j+1] - heights[i][j])
                if efforts[i][j+1] > max(efforts[i][j], effort):
                    efforts[i][j+1] = max(efforts[i][j], effort)
                    q.append((i, j+1))

        return efforts[rows-1][cols-1]
