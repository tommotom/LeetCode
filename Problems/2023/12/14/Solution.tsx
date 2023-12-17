function onesMinusZeros(grid: number[][]): number[][] {
    const row = [...Array(grid.length)].map(_ => [0, 0]);
    const col = [...Array(grid[0].length)].map(_ => [0, 0]);
    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[0].length; j++) {
            if (grid[i][j] === 0) {
                row[i][0] += 1;
                col[j][0] += 1;
            } else {
                row[i][1] += 1;
                col[j][1] += 1;
            }
        }
    }
    const ans = [];
    for (let i = 0; i < grid.length; i++) {
        ans.push([]);
        for (let j = 0; j < grid[0].length; j++) {
            ans[i].push(row[i][1] + col[j][1] - row[i][0] - col[j][0]);
        }
    }
    return ans;
};
