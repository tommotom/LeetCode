function countHomogenous(s: string): number {
    const mod = 1000000007;
    let last = '', contiguous = 1, ans = 0;
    for (let i = 0; i < s.length; i++) {
        if (last === s.charAt(i)) {
            contiguous++;
        } else {
            contiguous = 1;
            last = s.charAt(i);
        }
        ans = (ans + contiguous) % mod;
    }
    return ans;
};
