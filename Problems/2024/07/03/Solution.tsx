function minDifference(nums: number[]): number {
    const n = nums.length;
    if (n <= 4) {
        return 0;
    }
    nums.sort((a, b) => a - b);
    return [
        nums[n-1] - nums[3],
        nums[n-2] - nums[2],
        nums[n-3] - nums[1],
        nums[n-4] - nums[0]
    ].reduce((a, b) => Math.min(a, b));
};
