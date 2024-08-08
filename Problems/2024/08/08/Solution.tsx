function spiralMatrixIII(rows: number, cols: number, rStart: number, cStart: number): number[][] {
    const dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]];
    let r = rStart, c = cStart, i = 0, len = 1;
    const ans = [];
    while (ans.length < rows * cols) {
        for (let l = 0; l < len; l++) {
            if (0 <= r && r < rows && 0 <= c && c < cols) {
                ans.push([r, c]);
            }
            c += dirs[i][0];
            r += dirs[i][1];
        }
        if (i % 2 === 1) {
            len++;
        }
        i = (i + 1) % 4;
    }
    return ans;
};
