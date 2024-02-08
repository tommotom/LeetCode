function numSquares(n: number): number {
    const dp = Array(n+1).fill(Number.MAX_SAFE_INTEGER);
    dp[0] = 0;
    for (let i = 1; i <= n; i++) {
        let num = 1;
        while (i - Math.pow(num, 2) >= 0) {
            dp[i] = Math.min(dp[i], dp[i - Math.pow(num, 2)] + 1);
            num++;
        }
    }
    return dp[n];
};
