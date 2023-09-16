function minimumEffortPath(heights: number[][]): number {
    const m = heights.length, n = heights[0].length;
    const dp = [...Array(m)].map(_ => [...Array(n)].map(_ => Number.MAX_SAFE_INTEGER));
    dp[0][0] = 0;

    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    function dfs(i: number, j: number): void {
        for (const d of dirs) {
            const I = i + d[0], J = j + d[1];
            if (I < 0 || I === m || J < 0 || J === n) {
                continue;
            }
            const diff = Math.abs(heights[I][J] - heights[i][j]);
            const score = Math.max(dp[i][j], diff);
            if (score < dp[I][J]) {
                dp[I][J] = score;
                dfs(I, J)
            }
        }
    }
    dfs(0, 0);
    return dp[m-1][n-1];
};
