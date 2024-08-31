function countSubIslands(grid1: number[][], grid2: number[][]): number {
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    const m = grid1.length;
    const n = grid1[0].length;
    const isOut = (i, j) => i < 0 || i === m || j < 0 || j === n;
    const islands1 = [];
    const dfs1 = (i, j, id) => {
        if (isOut(i, j) || grid1[i][j] <= 0) {
            return;
        }
        grid1[i][j] = id;
        for (const [di, dj] of dirs) {
            dfs1(i + di, j + dj, id);
        }
    };

    let id = -1;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid1[i][j] === 1) {
                islands1.push([]);
                dfs1(i, j, id--);
            }
        }
    }

    const dfs2 = (i, j, id, isValid) => {
        if (isOut(i, j) || grid2[i][j] === 0) {
            return isValid;
        }
        if (grid1[i][j] !== id) {
            isValid = false;
        }
        grid2[i][j] = 0;
        for (const [di, dj] of dirs) {
            if (!dfs2(i + di, j + dj, id, isValid)) {
                isValid = false;
            };
        }
        return isValid;
    }

    let ans = 0;

    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid2[i][j] === 0) {
                continue;
            }
            if (dfs2(i, j, grid1[i][j], true) && grid1[i][j] !== 0) {
                ans++;
            }
        }
    }

    return ans;
};
