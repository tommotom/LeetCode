function minSubarray(nums: number[], p: number): number {
    const n = nums.length;
    const sum = nums.reduce((a, b) => (a + b) % p);
    const target = sum % p;
    if (target === 0) {
        return 0;
    }

    const seen = new Map([[0, -1]]);
    let cur = 0, ans = n;
    for (let i = 0; i < n; i++) {
        cur = (cur + nums[i]) % p;
        const tmp = (cur - target + p) % p;
        if (seen.has(tmp)) {
            ans = Math.min(ans, i - seen.get(tmp));
        }
        seen.set(cur, i);
    }

    return ans === n ? -1 : ans;
};
