function countFairPairs(nums: number[], lower: number, upper: number): number {
    nums.sort((a, b) => a - b);
    const bisectL = (l, r, target) => {
        while (l < r) {
            const m = l + Math.floor((r - l) / 2);
            if (nums[m] < target) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
    const bisectR = (l, r, target) => {
        while (l < r) {
            const m = l + Math.floor((r - l) / 2);
            if (nums[m] <= target) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return l;
    }
    let ans = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        const l = bisectL(i+1, nums.length, lower - nums[i]);
        const r = bisectR(i+1, nums.length, upper - nums[i]);
        if (nums[i] + nums[l] < lower) {
            continue;
        }
        ans += nums[i] + nums[r] <= upper ? r - l + 1: r - l;
    }
    return ans;
};
