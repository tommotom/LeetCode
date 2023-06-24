function tallestBillboard(rods: number[]): number {
    const total = rods.reduce((a, b) => a + b);
    const dp = new Array(total+1);
    dp.fill(-1);
    dp[0] = 0;

    for (const rod of rods) {
        const copy = dp.concat();
        for (let i = 0; i < total - rod + 1; i++) {
            if (copy[i] === -1) {continue;}
            dp[i+rod] = Math.max(dp[i+rod], copy[i]);
            dp[Math.abs(i-rod)] = Math.max(dp[Math.abs(i-rod)], copy[i] + Math.min(i, rod));
        }
    }
    return dp[0];
};
