function numSubmatrixSumTarget(M: number[][], target: number): number {
    const rows = M.length, cols = M[0].length;
    for (const row of M) {
        for (let c = 1; c < cols; c++) {
            row[c] += row[c-1]
        }
    }

    let ans = 0;
    for (let i = 0; i < cols; i++) {
        for (let j = i; j < cols; j++) {
            const c = new Map();
            c.set(0, 1);
            let cur = 0;
            for (let k = 0; k < rows; k++) {
                cur += M[k][j] - (i > 0 ? M[k][i-1] : 0);
                ans += c.has(cur - target) ? c.get(cur - target) : 0;
                if (!c.has(cur)) {
                    c.set(cur, 0);
                }
                c.set(cur, c.get(cur) + 1);
            }
        }
    }
    return ans;
};
