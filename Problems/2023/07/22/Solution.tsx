function knightProbability(n: number, k: number, row: number, column: number): number {

    function isOnTheBoard(r: number, c: number): boolean {
        return 0 <= r && r < n && 0 <= c && c < n;
    }

    function createMatrix(): number[][] {
        const mat = [];
        for (let r = 0; r < n; r++) {
            const row = []
            for (let c = 0; c < n; c++) {
                row.push(0);
            }
            mat.push(row);
        }
        return mat;
    }

    let pos = createMatrix();
    pos[row][column] = 1;

    const dirs = [[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2]];
    for (let i = 0; i < k; i++) {
        const next = createMatrix();
        for (let r = 0; r < n; r++) {
            for (let c = 0; c < n; c++) {
                if (pos[r][c] === 0) {
                    continue;
                }
                for (const d of dirs) {
                    if (!isOnTheBoard(r+d[0], c+d[1])) {
                        continue;
                    }
                    next[r+d[0]][c+d[1]] += pos[r][c];
                }
            }
        }
        pos = next;
    }

    let count = 0;
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            count += pos[r][c];
        }
    }

    return count / Math.pow(8, k);
};
