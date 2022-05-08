class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        sets = [[set() for _ in range(cols)] for __ in range(rows)]
        sets[0][0].add(1 if grid[0][0] == '(' else -1)
        for i in range(rows):
            for j in range(cols):
                if i > 0:
                    for num in sets[i-1][j]:
                        if num < 0: continue
                        if grid[i][j] == '(':
                            sets[i][j].add(num + 1)
                        else:
                            sets[i][j].add(num - 1)
                if j > 0:
                    for num in sets[i][j-1]:
                        if num < 0: continue
                        if grid[i][j] == '(':
                            sets[i][j].add(num + 1)
                        else:
                            sets[i][j].add(num - 1)
        return 0 in sets[rows-1][cols-1]
