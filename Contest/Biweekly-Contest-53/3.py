class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        def valid(i, j, length):
            nonlocal grid, rows, cols
            if j - length < 0 or j + length >= cols or i + 2*length >= rows: return False
            return True

        def add(i, j, length):
            nonlocal grid, rows, cols
            ret = grid[i][j]
            for l in range(1, length+1):
                ret += grid[i+l][j-l] + grid[i+l][j+l]
            for l in range(1, length):
                ret += grid[i+2*length-l][j-l] + grid[i+2*length-l][j+l]
            return ret + grid[i+2*length][j]

        rhombus = []
        for i in range(rows):
            for j in range(cols):
                rhombus.append(grid[i][j])
                length = 1
                while valid(i, j, length):
                    rhombus.append(add(i, j, length))
                    length += 1
        rhombus = sorted(list(set(rhombus)), reverse=True)
        if len(rhombus) < 3:
            return rhombus
        return rhombus[:3]
