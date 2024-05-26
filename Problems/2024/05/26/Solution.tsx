function checkRecord(n: number): number {
    const mod: bigint = 1000000007n;
    const dp: bigint[][] = Array(n+1).fill(0).map(_ => Array(3).fill(0n));
    dp[0][0] = 1n;
    for (let i = 1; i <= n; i++) {
        dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % mod;
        dp[i][1] = dp[i-1][0];
        dp[i][2] = dp[i-1][1];
    }

    const sum: bigint[] = dp.map(col => (col[0] + col[1] + col[2]) % mod);
    let ans: bigint = 0n;
    for (let i = 1; i <= n; i++) {
        ans += sum[i-1] * sum[n-i];
        ans %= mod;
    }
    return Number((ans + sum[n]) % mod);
};
