class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0: return False

        n = len(grid)
        arr = [None for _ in range(n*n)]
        for i in range(n):
            for j in range(n):
                arr[grid[i][j]] = (i, j)

        moves = set([(1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2)])
        for i in range(len(arr)-1):
            diff = (arr[i+1][0]-arr[i][0], arr[i+1][1]-arr[i][1])
            if diff not in moves: return False
        return True
