function smallestDistancePair(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);

    const count = t => {
        let j = 1, ret = 0;
        for (let i = 0; i < nums.length-1; i++) {
            while (nums[j] - nums[i] <= t) {
                j++;
            }
            ret += j - i - 1;
        }
        return ret;
    }

    const n = nums.length;
    let l = 0, r = nums[nums.length-1] - nums[0];
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (count(m) < k) {
            l = m + 1;
        } else {
            r = m;
        }
    }

    return l;
};
