function updateMatrix(mat: number[][]): number[][] {
    const m = mat.length, n = mat[0].length;
    const ret = [...Array(m)].map(_ => [...Array(n)].map(_ => m*n));
    const q = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (mat[i][j] === 0) {
                q.push([i, j, 0]);
            }
        }
    }

    const dirs = [[0,1], [0,-1], [1,0], [-1,0]];
    while (q.length > 0) {
        const [i, j, d] = q.shift();
        if (ret[i][j] <= d) {
            continue;
        }
        ret[i][j] = d;
        for (const dir of dirs) {
            if (i + dir[0] < 0 || i + dir[0] === m || j + dir[1] < 0 || j + dir[1] === n) {
                continue;
            }
            q.push([i + dir[0], j + dir[1], d + 1]);
        }
    }

    return ret;
};
