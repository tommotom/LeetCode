class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def search(r, c, i, grid, island):
            nonlocal rows, cols
            grid[r][c] = i+2
            island[i].add((r,c))
            if r > 0 and grid[r-1][c] == 1:
                search(r-1, c, i, grid, island)
            if c > 0 and grid[r][c-1] == 1:
                search(r, c-1, i, grid, island)
            if r+1 < rows and grid[r+1][c] == 1:
                search(r+1, c, i, grid, island)
            if c+1 < cols and grid[r][c+1] == 1:
                search(r, c+1, i, grid, island)


        rows, cols = len(grid1), len(grid1[0])
        island1 = []
        for i in range(rows):
            for j in range(cols):
                if grid1[i][j] == 1:
                    island1.append(set())
                    idx = len(island1)-1
                    search(i, j, idx, grid1, island1)
        ans = 0
        island2 = []
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    island2.append(set())
                    idx = len(island2)-1
                    search(i, j, idx, grid2, island2)
                    if grid1[i][j] > 0 and island1[grid1[i][j]-2] >= island2[idx]:
                        ans += 1
        return ans
