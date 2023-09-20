function minOperations(nums: number[], x: number): number {
    const n = nums.length;
    let r = n;
    while (r > 0 && x > 0) {
        x -= nums[--r];
    }
    if (x > 0) {
        return -1;
    }
    let ans = x === 0 ? n - r : Number.MAX_SAFE_INTEGER;
    for (let l = 0; l < n; l++) {
        x -= nums[l];
        while (r < n && x < 0) {
            x += nums[r++];
        }
        if (x === 0) {
            ans = Math.min(ans, l+1 + (n-r));
        }
    }

    return ans === Number.MAX_SAFE_INTEGER ? -1 : ans;
};
