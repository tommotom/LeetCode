function countMaxOrSubsets(nums: number[]): number {
    const n = nums.length;
    const maximum = nums.reduce((a, b) => a | b);
    let ans = 0;
    for (let bit = 1; bit <= Math.pow(2, n); bit++) {
        let num = 0;
        for (let i = 0; i < n; i++) {
            if (((1<<i) & bit) > 0) {
                num |= nums[i];
            }
        }
        if (num === maximum) {
            ans++;
        }
    }
    return ans;
};
