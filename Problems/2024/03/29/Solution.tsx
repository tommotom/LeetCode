function countSubarrays(nums: number[], k: number): number {
    const M = nums.reduce((a, b) => Math.max(a, b));
    const idx = [];
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === M) {
            idx.push(i);
        }
        const freq = idx.length;
        if (freq >= k) {
            ans += idx[idx.length-k] + 1
        }
    }
    return ans;
};
