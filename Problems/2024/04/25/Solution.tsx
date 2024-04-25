function longestIdealString(s: string, k: number): number {
    const indexOf = c => c.charCodeAt(0) - 'a'.charCodeAt(0);

    let last = Array(26).fill(0);
    for (let i = 0; i < s.length; i++) {
        const dp = last.concat();
        const j = indexOf(s.charAt(i));
        let l = Math.max(0, j - k);
        while (l < 26 && l <= j + k) {
            dp[j] = Math.max(dp[j], last[l] + 1);
            l++;
        }
        last = dp;
    }

    return last.reduce((a, b) => Math.max(a, b));
};
