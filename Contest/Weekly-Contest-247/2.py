class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        def rotate(layer):
            nonlocal grid, k, rows, cols
            tmp = grid[layer][layer]
            for c in range(layer, cols - layer - 1):
                grid[layer][c] = grid[layer][c+1]
            for r in range(layer, rows - layer - 1):
                grid[r][cols-layer-1] = grid[r+1][cols-layer-1]
            for c in range(cols - layer - 1, layer, -1):
                grid[rows-layer-1][c] = grid[rows-layer-1][c-1]
            for r in range(rows - layer - 1, layer,  -1):
                grid[r][layer] = grid[r-1][layer]
            grid[layer+1][layer] = tmp
            return grid

        for layer in range(min(rows//2, cols//2)):
            way = ((rows-2*layer) + (cols-2*layer))*2-4
            for _ in range(k%way):
                rotate(layer)
        return grid
