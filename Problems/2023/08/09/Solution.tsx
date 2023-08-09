function minimizeMax(nums: number[], p: number): number {
    nums.sort((a, b) => a - b);
    let l = 0, r = nums[nums.length-1] - nums[0];
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        let count = 0;
        for (let i = 0; i < nums.length-1; i++) {
            if (nums[i+1] - nums[i] <= m) {
                count++;
                i++;
            }
        }
        if (count < p) {
            l = m + 1;
        } else {
            r = m;
        }
    }
    return l;
};
