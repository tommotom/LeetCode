function myPow(x: number, n: number): number {
    const memo: Map<number, number> = new Map();

    function helper(m: number): number {
        if (memo.has(m)) {
            return memo.get(m);
        }
        if (m === 0) {
            return 1;
        }
        if (m === 1) {
            return x;
        }
        if (m < 0) {
            return 1 / helper(-m);
        }
        if (m % 2 === 0) {
            const tmp = helper(Math.floor(m / 2));
            memo.set(m, tmp * tmp);
        } else {
            memo.set(m, x * helper(m - 1));
        }
        return memo.get(m);
    }

    return helper(n);
};
