function searchRange(nums: number[], target: number): number[] {
    let l = 0, r = nums.length;
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (nums[m] < target) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    if (l === nums.length || nums[l] !== target) {
        return [-1, -1];
    }
    const start = l;
    l = 0, r = nums.length;
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (nums[m] <= target) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return [start, l-1];
};
