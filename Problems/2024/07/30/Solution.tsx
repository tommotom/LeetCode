function minimumDeletions(s: string): number {
    const dp = Array(s.length + 1).fill(0);
    let b = 0;
    for (let i = 0; i < s.length; i++) {
        if (s.charAt(i) === 'b') {
            b++;
            dp[i+1] = dp[i];
        } else {
            dp[i+1] = Math.min(dp[i] + 1, b);
        }
    }
    return dp[s.length];
};
