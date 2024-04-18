function islandPerimeter(grid: number[][]): number {
    const count = (r, c) => {
        if (grid[r][c] === 0) {
            return 0;
        }
        let ret = 0;
        ret += r > 0 ? 1 - grid[r-1][c] : 1;
        ret += c > 0 ? 1 - grid[r][c-1] : 1;
        ret += r+1 < grid.length ? 1 - grid[r+1][c] : 1;
        ret += c+1 < grid[0].length ? 1 - grid[r][c+1] : 1;
        return ret;
    }

    let ans = 0;
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            ans += count(i, j);
        }
    }
    return ans;
};
