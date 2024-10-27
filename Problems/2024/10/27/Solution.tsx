function countSquares(matrix: number[][]): number {
    const n = matrix.length, m = matrix[0].length;
    const rows = Array(n).fill(0).map(_ => Array(m).fill(0));
    const cols = Array(n).fill(0).map(_ => Array(m).fill(0));

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (matrix[i][j] === 1) {
                rows[i][j] = (j > 0 && matrix[i][j-1] === 1 ? rows[i][j-1] : 0) + 1;
                cols[i][j] = (i > 0 && matrix[i-1][j] === 1 ? cols[i-1][j] : 0) + 1;
            }
        }
    }

    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < m; j++) {
            if (matrix[i][j] === 0) {
                continue;
            }
            let r = 1;
            while (i >= r && rows[i-r][j] > 0 && rows[i-r][j] > r) {
                r++;
            }
            let c = 1;
            while (j >= c && cols[i][j-c] > 0 && cols[i][j-c] > c) {
                c++;
            }
            ans += Math.min(r, c);
        }
    }

    return ans;
};
