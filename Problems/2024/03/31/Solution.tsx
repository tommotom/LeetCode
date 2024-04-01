function countSubarrays(nums: number[], minK: number, maxK: number): number {
    let ans = 0;
    let bad = -1, left = -1, right = -1;
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (num < minK || maxK < num) {
            bad = i;
        }
        if (num === minK) {
            left = i;
        }
        if (num === maxK) {
            right = i;
        }
        ans += Math.max(0, Math.min(left, right) - bad);
    }
    return ans;
};
