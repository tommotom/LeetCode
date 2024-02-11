function cherryPickup(grid: number[][]): number {

    const memo = new Map();

    function helper(r: number, i: number, j: number): number {
        if (r === grid.length) {
            return 0;
        }
        const key = [r, i, j].join(",");
        if (memo.has(key)) {
            return memo.get(key);
        }
        const cur = grid[r][i] + (i !== j ? grid[r][j] : 0);
        let next = 0;
        for (let I = i-1; I < i+2; I++) {
            if (I < 0 || I === grid[r].length) {
                continue;
            }
            for (let J = j-1; J < j+2; J++) {
                if (J < 0 || J === grid[r].length) {
                    continue;
                }
                next = Math.max(next, helper(r+1, I, J));
            }
        }
        memo.set(key, cur + next);
        return cur + next;
    }

    return helper(0, 0, grid[0].length-1);
};
