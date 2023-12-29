function getLengthOfOptimalCompression(s: string, k: number): number {
    function runLength(cnt: number): number {
        if (cnt >= 100) {
            return 3;
        } else if (cnt >= 10) {
            return 2;
        } else if (cnt >= 2) {
            return 1;
        }
        return 0;
    }
    const dp = Array.from({ length: 110 }, () => Array(110).fill(9999));
    dp[0][0] = 0;
    for (let i = 1; i <= s.length; i++) {
        for (let j = 0; j <= k; j++) {
            let del = 0, cnt = 0;
            for (let l = i; l >= 1; l--) {
                if (s.charAt(i-1) === s.charAt(l-1)) {
                    cnt++;
                } else {
                    del++;
                }
                if (j - del >= 0) {
                    dp[i][j] = Math.min(dp[i][j], dp[l-1][j-del] + 1 + runLength(cnt));
                }
            }
            if (j > 0) {
                dp[i][j] = Math.min(dp[i][j], dp[i-1][j-1]);
            }
        }
    }
    return dp[s.length][k];

};
