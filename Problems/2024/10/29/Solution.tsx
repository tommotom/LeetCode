function maxMoves(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const arr = Array(m).fill(0).map(_ => Array(n).fill(0));
    for (let c = 0; c < n-1; c++) {
        for (let r = 0; r < m; r++) {
            if (arr[r][c] < c) {
                continue;
            }
            if (r > 0 && grid[r][c] < grid[r-1][c+1]) {
                arr[r-1][c+1] = Math.max(arr[r-1][c+1], arr[r][c] + 1);
            }
            if (grid[r][c] < grid[r][c+1]) {
                arr[r][c+1] = Math.max(arr[r][c+1], arr[r][c] + 1);
            }
            if (r+1 < m && grid[r][c] < grid[r+1][c+1]) {
                arr[r+1][c+1] = Math.max(arr[r+1][c+1], arr[r][c] + 1);
            }
        }
    }
    return arr.reduce((acc, cur) => Math.max(cur.reduce((a, b) => Math.max(a, b)), acc), 0);
};
