function soupServings(n: number): number {
    if (n > 4800) {
        return 1;
    }

    const memo: Map<string, number> = new Map();
    function helper(a: number, b: number) {
        const key = a + "," + b;
        if (memo.has(key)) {
            return memo.get(key);
        }
        if (a <= 0 && b <= 0) {
            return 0.5;
        } else if (a <= 0) {
            return 1;
        } else if (b <= 0) {
            return 0;
        }
        const ret = (helper(a-100, b) + helper(a-75, b-25) + helper(a-50, b-50) + helper(a-25, b-75)) / 4;
        memo.set(key, ret);
        return ret;
    }

    return helper(n, n);
};
