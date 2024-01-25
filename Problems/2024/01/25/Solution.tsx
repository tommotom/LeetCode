function longestCommonSubsequence(text1: string, text2: string): number {
    const len1 = text1.length, len2 = text2.length;
    const dp = Array(len1+1).fill(0).map(() => Array(len2+1).fill(0));
    for (let i = 0; i < len1; i++) {
        for (let j = 0; j < len2; j++) {
            if (text1.charAt(i) === text2.charAt(j)) {
                dp[i+1][j+1] = dp[i][j] + 1;
            } else {
                dp[i+1][j+1] = Math.max(dp[i][j+1], dp[i+1][j]);
            }
        }
    }
    return dp[len1][len2];
};
