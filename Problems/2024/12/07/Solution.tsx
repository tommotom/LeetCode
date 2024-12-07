function minimumSize(nums: number[], maxOperations: number): number {
    let l = 1, r = nums.reduce((a, b) => Math.max(a, b));
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (nums.reduce((a, b) => a + Math.ceil(b / m) - 1, 0) <= maxOperations) {
            r = m;
        } else {
            l = m + 1;
        }
    }
    return l;
};
