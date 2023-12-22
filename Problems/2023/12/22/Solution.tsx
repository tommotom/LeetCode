function maxScore(s: string): number {
    let ones = 0;
    for (const c of s) {
        if (c === '1') {
            ones++;
        }
    }
    let zeros = 0, ans = 0;
    for (let i = 0; i < s.length-1; i++) {
        if (s.charAt(i) === '0') {
            zeros++;
        } else {
            ones--;
        }
        ans = Math.max(ans, ones + zeros);
    }
    return ans;
};
