function numOfArrays(n: number, m: number, k: number): number {
    const memo = new Map();
    const mod = 1000000007;
    function dp(i: number, val: number, cost: number): number {
        if (i === n) {
            return k === cost ? 1 : 0;
        }
        const key = i + " " + val + " " + cost;
        if (memo.has(key)) {
            return memo.get(key);
        }
        let ret = val * dp(i+1, val, cost) % mod;
        for (let num = val + 1; num <= m; num++) {
            ret += dp(i+1, num, cost+1);
            ret %= mod;
        }
        memo.set(key, ret);
        return ret;
    }
    return dp(0, 0, 0);
};
