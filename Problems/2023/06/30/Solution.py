class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def isPossible(day):
            nonlocal dirs
            matrix = [[0] * col for _ in range(row)]
            for r, c in cells[:day]:
                matrix[r-1][c-1] = 1

            q = deque()
            for c in range(col):
                if not matrix[0][c]: q.append((0, c))

            visited = set(q)
            while q:
                r, c = q.popleft()
                for d in dirs:
                    nextR, nextC = r + d[0], c + d[1]
                    if nextR == row: return True
                    if nextR == -1 or nextC == -1 or nextC == col: continue
                    if matrix[nextR][nextC]: continue
                    if (nextR, nextC) in visited: continue
                    q.append((nextR, nextC))
                    visited.add((nextR, nextC))
            return False

        l, r = 0, len(cells)
        while l < r:
            m = l + (r - l) // 2
            if isPossible(m):
                l = m + 1
            else:
                r = m
        return l - 1
