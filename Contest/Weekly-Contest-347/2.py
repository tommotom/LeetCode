class Solution:
    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        def topLeft(r, c, counter):
            if r < 0 or c < 0: return len(counter)
            counter[grid[r][c]] += 1
            return topLeft(r-1, c-1, counter)

        def bottomRight(r, c, counter):
            if r == len(grid) or c == len(grid[0]): return len(counter)
            counter[grid[r][c]] += 1
            return bottomRight(r+1, c+1, counter)

        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                ans[r][c] = abs(topLeft(r-1, c-1, defaultdict(int)) - bottomRight(r+1, c+1, defaultdict(int)))

        return ans
