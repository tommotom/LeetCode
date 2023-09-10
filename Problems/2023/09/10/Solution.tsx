function countOrders(n: number): number {
    const mod = 1000000007;
    const memo = new Map();
    function key(p, d) {
        return p.toString() + " " + d.toString();
    }
    function helper(p: number, d: number) {
        if (p === 0 && d === 0) {
            return 1;
        }
        const k = key(p, d);
        if (!memo.has(k)) {
            if (p === 0) {
                memo.set(k, (d * helper(p, d-1)) % mod);
            } else if (d === 0) {
                memo.set(k, (p * helper(p-1, d+1) % mod));
            } else {
                memo.set(k, (d * helper(p, d-1) + p * helper(p-1, d+1)) % mod);
            }
        }
        return memo.get(k);
    }
    return helper(n, 0);
};
