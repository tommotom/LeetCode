function nthUglyNumber(n: number): number {
    const dp = [1];
    let i2 = 0, i3 = 0, i5 = 0;
    let n2 = 2, n3 = 3, n5 = 5;
    for (let _ = 1; _ < n; _++) {
        const next = [n2, n3, n5].reduce((a, b) => Math.min(a, b));
        dp.push(next);
        if (next === n2) {
            n2 = dp[++i2] * 2;
        }
        if (next === n3) {
            n3 = dp[++i3] * 3;
        }
        if (next === n5) {
            n5 = dp[++i5] * 5;
        }
    }
    return dp[dp.length-1];
};
