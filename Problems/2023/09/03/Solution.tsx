const memo: Map<string, number> = new Map();

function uniquePaths(m: number, n: number): number {
    function key(m: number, n: number): string {
        return m.toString() + " " + n.toString();
    }
    if (m === 1 || n === 1) {
        return 1;
    }
    const k = key(m, n);
    if (!memo.has(k)) {
        memo.set(k, uniquePaths(m-1, n) + uniquePaths(m, n-1));
    }
    return memo.get(k);
};
