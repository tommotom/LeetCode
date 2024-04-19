function numIslands(grid: string[][]): number {
    let ans = 0;
    const m = grid.length, n = grid[0].length;
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    const dfs = (r, c) => {
        if (r < 0 || r === m || c < 0 || c === n) {
            return;
        }
        if (grid[r][c] === "0") {
            return;
        }
        grid[r][c] = "0";
        for (const [dr, dc] of dirs) {
            dfs(r + dr, c + dc);
        }
    }

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === "1") {
                ans++;
                dfs(i, j);
            }
        }
    }
    return ans;
};
