function minCost(nums: number[], cost: number[]): number {

    const calcCost = (nums, cost, target) => {
        let ret = 0;
        for (let i = 0; i < nums.length; i++) {
            ret += Math.abs(nums[i] - target) * cost[i];
        }
        return ret;
    }

    let l = nums.reduce((a, b) => Math.min(a, b));
    let r = nums.reduce((a, b) => Math.max(a, b));

    while (l < r) {
        const m = Math.floor(l + (r - l) / 2);
        const L = calcCost(nums, cost, m);
        const R = calcCost(nums, cost, m+1);
        if (L < R) {
            r = m;
        } else {
            l = m + 1;
        }
    }

    return calcCost(nums, cost, l);
};
