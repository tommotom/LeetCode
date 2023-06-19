function largestAltitude(gain: number[]): number {
    let ans = 0, cur = 0;
    for (const g of gain) {
        cur += g;
        ans = Math.max(ans, cur);
    }
    return ans;
};
