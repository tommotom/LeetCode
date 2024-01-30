function kInversePairs(n: number, k: number): number {
    const mod = 1000000007;
    let last = Array(k+1).fill(0);
    last[0] = 1;
    for (let i = 2; i <= n; i++) {
        const cur = Array(k+1).fill(0);
        cur[0] = 1;
        for (let j = 1; j <= k; j++) {
            let val = last[j] + mod - (j >= i ? last[j-i] : 0);
            val %= mod;
            cur[j] = (cur[j-1] + val) % mod;
        }
        last = cur;
    }
    return last[k];
};
