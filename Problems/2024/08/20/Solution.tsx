function stoneGameII(piles: number[]): number {
    const n = piles.length;
    const dp = Array(n+1).fill(0).map(_ => Array(n+1).fill(0));
    const suffix = Array(n+1).fill(0);
    for (let i = n-1; i >= 0; i--) {
        suffix[i] = suffix[i+1] + piles[i];
    }

    for (let i = 0; i < n+1; i++) {
        dp[i][n] = suffix[i];
    }

    for (let i = n-1; i >= 0; i--) {
        for (let j = n-1; j > 0; j--) {
            for (let X = 1; X < Math.min(2 * j, n - i) + 1; X++) {
                dp[i][j] = Math.max(dp[i][j], suffix[i] - dp[i+X][Math.max(j, X)]);
            }
        }
    }
    return dp[0][1];
};
