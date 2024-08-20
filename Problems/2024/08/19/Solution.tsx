function minSteps(n: number): number {
    const dp = Array(n+1).fill(Number.MAX_SAFE_INTEGER);
    dp[1] = 0
    for (let i = 1; i <= n; i++) {
        let copy = 1;
        for (let j = 2; i * j <= n; j++) {
            dp[i*j] = dp[i * (j-1)] + 1 + copy;
            copy = 0;
        }
    }
    return dp[n];
};
