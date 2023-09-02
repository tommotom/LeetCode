function minExtraChar(s: string, dictionary: string[]): number {
    const dp = [0];
    for (let i = 0; i < s.length; i++) {
        let count = dp[dp.length-1] + 1;
        for (const word of dictionary) {
            if (word.length > i + 1) {
                continue;
            }
            if (s.substring(i-word.length+1, i+1) === word) {
                count = Math.min(count, dp[i - word.length + 1]);
            }
        }
        dp.push(count);
    }
    return dp[dp.length-1];
};
