function climbStairs(n: number): number {
    const dp = [1];
    for (let i = 1; i <= n; i++) {
        dp.push(dp[i-1]);
        if (i-2 >= 0) {
            dp[i] += dp[i-2];
        }
    }
    return dp[dp.length-1];
};
