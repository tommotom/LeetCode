function firstMissingPositive(nums: number[]): number {
    let i = 0;
    while (i < nums.length) {
        const idx = nums[i] - 1;
        if (0 < nums[i] && nums[i] <= nums.length && nums[i] !== nums[idx]) {
            const tmp = nums[i];
            nums[i] = nums[idx];
            nums[idx] = tmp;
        } else {
            i++;
        }
    }
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== i + 1) {
            return i + 1;
        }
    }
    return nums.length + 1;
};
