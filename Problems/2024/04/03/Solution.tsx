function exist(board: string[][], word: string): boolean {
    const dirs = [[0,1], [0,-1], [1,0], [-1,0]];
    const m = board.length, n = board[0].length;
    const key = (r, c) => `${r}-${c}`;

    function dfs(r: number, c: number, used: Set<string>, i: number) {
        if (word.charAt(i) !== board[r][c]) {
            return false;
        }
        if (i === word.length - 1) {
            return true;
        }
        used.add(key(r, c));
        for (const [dr, dc] of dirs) {
            if (r + dr < 0 || r + dr === m || c + dc < 0 || c + dc === n) {
                continue;
            }
            if (used.has(key(r + dr, c + dc))) {
                continue;
            }
            if (dfs(r + dr, c + dc, used, i+1)) {
                return true;
            }
        }
        used.delete(key(r, c));
        return false;
    }

    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (dfs(r, c, new Set(), 0)) {
                return true;
            }
        }
    }

    return false;
};
