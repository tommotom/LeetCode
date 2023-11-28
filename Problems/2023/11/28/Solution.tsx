function numberOfWays(corridor: string): number {
    const memo = new Map();
    const mod = 1000000007;
    function helper(i: number, count: number): number {
        if (i === corridor.length) {
            return count === 2 ? 1 : 0;
        }
        const key = i.toString() + " " + count.toString();
        if (memo.has(key)) {
            return memo.get(key);
        }
        count += corridor.charAt(i) === 'S' ? 1 : 0;
        if (count === 3) {
            return 0;
        } else if (count === 2) {
            memo.set(key, (helper(i+1, 0) + helper(i+1, count)) % mod);
        } else {
            memo.set(key, helper(i+1, count) % mod);
        }
        return memo.get(key);
    }
    return helper(0, 0);
};
