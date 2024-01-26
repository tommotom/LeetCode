function findPaths(m: number, n: number, maxMove: number, startRow: number, startColumn: number): number {

    function isOut(row: number, col: number): boolean {
        return row < 0 || m <= row || col < 0 || n <= col;
    }

    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]], mod = 1000000007;
    let count = Array(m).fill(0).map(() => Array(n).fill(0)), ans = 0;
    count[startRow][startColumn] = 1;
    for (let M = 0; M < maxMove; M++) {
        const next = Array(m).fill(0).map(() => Array(n).fill(0));
        for (let r = 0; r < m; r++) {
            for (let c = 0; c < n; c++) {
                if (count[r][c] === 0) {
                    continue;
                }
                for (const [dr, dc] of dirs) {
                    if (isOut(r + dr, c + dc)) {
                        ans += count[r][c];
                        ans %= mod
                    } else {
                        next[r+dr][c+dc] += count[r][c];
                        next[r+dr][c+dc] %= mod;
                    }
                }
            }
        }
        count = next;
    }
    return ans;
};
