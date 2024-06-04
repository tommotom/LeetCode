function longestPalindrome(s: string): number {
    const counter = new Map();
    for (const c of s) {
        if (!counter.has(c)) {
            counter.set(c, 0);
        }
        counter.set(c, counter.get(c) + 1);
    }
    let ans = 0, odd = false;
    for (const count of counter.values()) {
        ans += Math.floor(count / 2) * 2;
        if (!odd && count % 2 === 1) {
            ans++;
            odd = true;
        }
    }
    return ans;
};
