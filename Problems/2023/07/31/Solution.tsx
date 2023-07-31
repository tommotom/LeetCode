function minimumDeleteSum(s1: string, s2: string): number {
    const l1 = s1.length, l2 = s2.length;

    const dp: number[][] = []
    for (let i = 0; i <= l1; i++) {
        const row: number[] = [i > 0 ? dp[i-1][0] + s1.charCodeAt(i-1) : 0];
        for (let j = 0; j < l2; j++) {
            row.push(i === 0 ? row[j] + s2.charCodeAt(j) : 0);
        }
        dp.push(row);
    }

    for (let i = 0; i < l1; i++) {
        for (let j = 0; j < l2; j++) {
            if (s1[i] === s2[j]) {
                dp[i+1][j+1] = dp[i][j]
            } else {
                dp[i+1][j+1] = Math.min(dp[i][j+1] + s1.charCodeAt(i), dp[i+1][j] + s2.charCodeAt(j))
            }
        }
    }

    return dp[l1][l2];
};
