function countUnguarded(m: number, n: number, guards: number[][], walls: number[][]): number {
    const UNGUARDED = 0, GUARDED = 1, GUARD = 2, WALL = 3;
    const grid = Array(m).fill(0).map(_ => Array(n).fill(0));

    const updateCellVisibility = (r, c, isGuardLine) => {
        if (grid[r][c] === GUARD) {
            return true;
        }

        if (grid[r][c] === WALL) {
            return false;
        }

        if (isGuardLine) {
            grid[r][c] = GUARDED;
        }

        return isGuardLine
    }

    for (const [r, c] of guards) {
        grid[r][c] = GUARD;
    }

    for (const [r, c] of walls) {
        grid[r][c] = WALL;
    }

    for (let r = 0; r < m; r++) {
        let isGuardLine = grid[r][0] === GUARD;
        for (let c = 1; c < n; c++) {
            isGuardLine = updateCellVisibility(r, c, isGuardLine);
        }

        isGuardLine = grid[r][n-1] === GUARD;
        for (let c = n - 2; c >= 0; c--) {
            isGuardLine = updateCellVisibility(r, c, isGuardLine);
        }
    }

    for (let c = 0; c < n; c++) {
        let isGuardLine = grid[0][c] === GUARD;
        for (let r = 1; r < m; r++) {
            isGuardLine = updateCellVisibility(r, c, isGuardLine);
        }

        isGuardLine = grid[m-1][c] === GUARD;
        for (let r = m - 2; r >= 0; r--) {
            isGuardLine = updateCellVisibility(r, c, isGuardLine);
        }
    }

    let ans = 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            ans += grid[r][c] === UNGUARDED ? 1 : 0;
        }
    }

    return ans;
};
