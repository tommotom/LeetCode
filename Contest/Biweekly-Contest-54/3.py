class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row = [[0] * n for _ in range(m)]
        col = [[0] * n for _ in range(m)]
        dia1 = [[0] * n for _ in range(m)]
        dia2 = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                row[i][j] += grid[i][j] + (row[i][j-1] if j > 0 else 0)
        for i in range(m):
            for j in range(n):
                col[i][j] += grid[i][j] + (col[i-1][j] if i > 0 else 0)
        for i in range(m):
            for j in range(n):
                dia1[i][j] += grid[i][j] + (dia1[i-1][j-1] if i > 0 and j > 0 else 0)
        for i in range(m):
            for j in range(n):
                dia2[i][j] += grid[i][j] + (dia2[i-1][j+1] if i > 0 and j < n-1 else 0)
                
        for size in range(min(m, n), 1, -1):
            for i in range(m-size+1):
                for j in range(n-size+1):
                    row_sum = row[i][j+size-1] - (row[i][j-1] if j > 0 else 0)
                    for r in range(1,size):
                        if not row_sum == row[i+r][j+size-1] - (row[i+r][j-1] if j > 0 else 0):
                            break
                    else:
                        for c in range(size):
                            if not row_sum == col[i+size-1][j+c] - (col[i-1][j+c] if i > 0 else 0):
                                break
                        else:
                            if dia1[i+size-1][j+size-1] - (dia1[i-1][j-1] if i > 0 and j > 0 else 0) == row_sum and dia2[i+size-1][j] - (dia2[i-1][j+size] if i > 0 and j+size < n else 0) == row_sum: return size
        return 1
