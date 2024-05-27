function specialArray(nums: number[]): number {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        if (i > 0 && nums[i-1] === nums[i]) {
            continue;
        }
        const x = n - i;
        if ((i === 0 || nums[i-1] < x) && x <= nums[i]) {
            return x;
        }
    }
    return -1;
};
