function findWinners(matches: number[][]): number[][] {
    const lost = new Map();
    for (const [w, l] of matches) {
        if (!lost.has(w)) {
            lost.set(w, 0);
        }
        if (!lost.has(l)) {
            lost.set(l, 0);
        }
        lost.set(l, lost.get(l) + 1);
    }

    const ans = [[], []];
    for (const l of lost.keys()) {
        if (lost.get(l) === 0) {
            ans[0].push(l);
        } else if (lost.get(l) === 1) {
            ans[1].push(l);
        }
    }
    ans[0].sort((a, b) => a - b);
    ans[1].sort((a, b) => a - b);
    return ans;
};
