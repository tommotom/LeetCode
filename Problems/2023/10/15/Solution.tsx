function numWays(steps: number, arrLen: number): number {
    const memo = new Map();
    const mod = 1000000007;
    function dp(i: number, s: number): number {
        if (s === steps) {
            return i === 0 ? 1 : 0;
        }
        if (i < 0 || i >= arrLen) {
            return 0;
        }
        const key = i + " " + s;
        if (!memo.has(key)) {
            memo.set(key, (dp(i-1, s+1) + dp(i, s+1) + dp(i+1, s+1))%mod)
        }
        return memo.get(key);
    }
    return dp(0, 0);
};
