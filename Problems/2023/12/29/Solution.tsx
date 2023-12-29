function minDifficulty(jobDifficulty: number[], d: number): number {
    const dp = Array.from({length:d+1}, () => new Array(jobDifficulty.length + 1).fill(Number.MAX_SAFE_INTEGER));
    dp[0][0] = 0;
    for (let i = 1; i <= d; i++) {
        for (let j = 1; j <= jobDifficulty.length; j++) {
            let M = 0;
            for (let k = j; k <= jobDifficulty.length; k++) {
                M = Math.max(M, jobDifficulty[k-1]);
                dp[i][k] = Math.min(dp[i][k], dp[i-1][j-1] + M);
            }
        }
    }
    return dp[d][jobDifficulty.length] === Number.MAX_SAFE_INTEGER ? -1 : dp[d][jobDifficulty.length];
};
