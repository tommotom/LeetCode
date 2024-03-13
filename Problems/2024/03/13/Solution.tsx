function pivotInteger(n: number): number {
    const rangeSum = (low: number, high: number) => (high - low + 1) * (low + high) / 2;
    let l = 1, r = n + 1;
    while (l < r) {
        let m = l + Math.floor((r - l) / 2);
        const down = rangeSum(1, m);
        const up = rangeSum(m, n);
        if (down < up) {
            l = m + 1;
        } else if (down > up) {
            r = m;
        } else {
            return m;
        }
    }
    return -1
};
