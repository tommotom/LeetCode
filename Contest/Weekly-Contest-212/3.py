from collections import deque
class Solution:
    INF = 10**9
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row, col = len(heights), len(heights[0])
        effort = [[self.INF] * col for _ in range(row)]
        q = deque([(0, 0)])
        effort[0][0] = 0
        while q:
            i, j = q.popleft()

            if i > 0:
                cost = max(abs(heights[i-1][j] - heights[i][j]), effort[i][j])
                if effort[i-1][j] > cost:
                    effort[i-1][j] = cost
                    q.append((i-1, j))

            if j > 0:
                cost = max(abs(heights[i][j-1] - heights[i][j]), effort[i][j])
                if effort[i][j-1] > cost:
                    effort[i][j-1] = cost
                    q.append((i, j-1))

            if i+1 < row:
                cost = max(abs(heights[i+1][j] - heights[i][j]), effort[i][j])
                if effort[i+1][j] > cost:
                    effort[i+1][j] = cost
                    q.append((i+1, j))

            if j+1 < col:
                cost = max(abs(heights[i][j+1] - heights[i][j]), effort[i][j])
                if effort[i][j+1] > cost:
                    effort[i][j+1] = cost
                    q.append((i, j+1))

        return effort[row-1][col-1]
