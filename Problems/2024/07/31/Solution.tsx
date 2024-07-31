function minHeightShelves(books: number[][], shelfWidth: number): number {
    const n = books.length;
    const dp = Array(n+1).fill(0).map(_ => Array(shelfWidth+1).fill(undefined));
    dp[0][0] = [0, 0];
    for (let i = 0; i < n; i++) {
        for (let j = 0; j <= shelfWidth; j++) {
            if (dp[i][j] === undefined) {
                continue;
            }
            if (j + books[i][0] <= shelfWidth) {
                dp[i+1][j+books[i][0]] = [dp[i][j][0], Math.max(dp[i][j][1], books[i][1])];
            }
            if (j > 0) {
                if (dp[i+1][books[i][0]] !== undefined && dp[i+1][books[i][0]][0] < dp[i][j][0] + dp[i][j][1]) {
                    continue;
                }
                dp[i+1][books[i][0]] = [dp[i][j][0] + dp[i][j][1], books[i][1]];
            }
        }
    }

    return dp[n].filter(cell => cell !== undefined).map(cell => cell[0] + cell[1]).reduce((a, b) => Math.min(a, b));
};
