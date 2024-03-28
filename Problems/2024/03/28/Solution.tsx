function maxSubarrayLength(nums: number[], k: number): number {
    const freq = new Map();
    let last = 0, ans = 0;
    for (let i = 0; i < nums.length; i++) {
        if (!freq.has(nums[i])) {
            freq.set(nums[i], [])
        }
        const q = freq.get(nums[i]);
        while (q.length > 0 && q[0] < last) {
            q.shift();
        }
        q.push(i);
        if (q.length > k) {
            last = q.shift() + 1;
        }
        ans = Math.max(ans, i - last + 1);
    }
    return ans;
};
