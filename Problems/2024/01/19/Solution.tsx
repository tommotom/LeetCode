function minFallingPathSum(matrix: number[][]): number {
    const n = matrix.length;
    const dp = new Array(n).fill(null).map(() => new Array(n).fill(null));
    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            let last = i === 0 ? 0 : Math.min(dp[i-1][j], j > 0 ? dp[i-1][j-1] : Number.MAX_SAFE_INTEGER, j+1 < n ? dp[i-1][j+1] : Number.MAX_SAFE_INTEGER);
            dp[i][j] = last + matrix[i][j];
        }
    }
    return dp[n-1].reduce((a, b) => Math.min(a, b));
};
