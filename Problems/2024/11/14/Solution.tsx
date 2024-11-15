function minimizedMaximum(n: number, quantities: number[]): number {
    const isValid = num => {
        return quantities.reduce((a, b) => a + Math.ceil(b / num), 0) <= n
    }

    let l = 1, r = quantities.reduce((a, b) => Math.max(a, b));
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (!isValid(m)) {
            l = m + 1;
        } else {
            r = m;
        }
    }

    return l;
};
