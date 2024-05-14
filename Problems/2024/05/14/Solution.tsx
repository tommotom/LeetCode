function getMaximumGold(grid: number[][]): number {
    const dirs = [[0,1], [0,-1], [1,0], [-1,0]];
    const m = grid.length, n = grid[0].length;

    const dfs = (i, j) => {
        const cur = grid[i][j];
        grid[i][j] = 0;
        let next = 0;
        for (const [di, dj] of dirs) {
            if (0 <= i + di && i + di < m && 0 <= j + dj && j + dj < n && grid[i+di][j+dj] > 0) {
                next = Math.max(next, dfs(i+di, j+dj));
            }
        }
        grid[i][j] = cur;
        return next + cur;
    };

    let ans = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] > 0) {
                ans = Math.max(ans, dfs(i, j));
            }
        }
    }
    return ans;
};
