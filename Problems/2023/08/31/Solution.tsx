function minTaps(n: number, ranges: number[]): number {
    const dp = [...Array(n+1)].map(_ => Number.MAX_SAFE_INTEGER);
    dp[0] = 0;

    for (let i = 0; i < n+1; i++) {
        const r = ranges[i];
        const int = [Math.max(0, i - r), Math.min(n, i + r)];
        for (let j = int[0] + 1; j < int[1] + 1; j++) {
            dp[j] = Math.min(dp[j], dp[int[0]] + 1);
        }
    }

    return dp[n] !== Number.MAX_SAFE_INTEGER ? dp[n] : -1;
};
