class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter = defaultdict(int)
        for row in grid:
            counter[tuple(row)] += 1

        ans = 0
        for c in range(len(grid[0])):
            arr = []
            for r in range(len(grid)):
                arr.append(grid[r][c])
            ans += counter[tuple(arr)]

        return ans
