function matrixScore(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    for (let i = 0; i < m; i++) {
        if (grid[i][0] === 1) {
            continue;
        }
        for (let j = 0; j < n; j++) {
            grid[i][j] = 1 - grid[i][j];
        }
    }

    for (let j = 1; j < n; j++) {
        let ones = 0;
        for (let i = 0; i < m; i++) {
            ones += grid[i][j];
        }
        if (ones < m - ones) {
            for (let i = 0; i < m; i++) {
                grid[i][j] = 1 - grid[i][j];
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < m; i++) {
        let num = 0;
        for (let j = 0; j < n; j++) {
            num = num * 2 + grid[i][j];
        }
        ans += num;
    }
    return ans;
};
