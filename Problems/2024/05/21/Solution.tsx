function subsets(nums: number[]): number[][] {
    const ans = [], n = nums.length;
    for (let bit = 0; bit < Math.pow(2, n); bit++) {
        const arr = [];
        for (let i = 0; i < n; i++) {
            if (bit & (1 << i)) {
                arr.push(nums[i]);
            }
        }
        ans.push(arr);
    }
    return ans;
};
