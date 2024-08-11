function minDays(grid: number[][]): number {
    const m = grid.length, n = grid[0].length;
    const dirs = [[0,1], [0,-1], [1,0], [-1,0]];

    const countIslands = () => {
        const visited = new Set();
        let count = 0;
        for (let r = 0; r < m; r++) {
            for (let c = 0; c < n; c++) {
                if (grid[r][c] === 1 && !visited.has(key(r, c))) {
                    dfs(r, c, visited);
                    count++;
                }
            }
        }
        return count;
    }

    const dfs = (r, c, visited) => {
        if (visited.has(key(r,c)) || !isValid(r, c) || grid[r][c] === 0) {
            return;
        }
        visited.add(key(r, c));
        for (const [dr, dc] of dirs) {
            dfs(r + dr, c + dc, visited);
        }
    }

    const isValid = (r, c) => {
        return 0 <= r && r < m && 0 <= c && c < n;
    }

    const key = (r, c) => {
        return `${r}, ${c}`;
    }

    if (countIslands() !== 1) {
        return 0;
    }

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (grid[r][c] === 1) {
                grid[r][c] = 0;
                if (countIslands() !== 1) {
                    return 1;
                }
                grid[r][c] = 1;
            }
        }
    }

    return 2;
};
