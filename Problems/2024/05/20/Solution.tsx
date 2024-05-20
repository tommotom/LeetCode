function subsetXORSum(nums: number[]): number {
    const n = nums.length;
    let ans = 0;
    for (let bit = 0; bit < Math.pow(2, n); bit++) {
        let xor = 0;
        for (let i = 0; i < n; i++) {
            if (bit & (1 << i)) {
                xor ^= nums[i];
            }
        }
        ans += xor;
    }
    return ans;
};
