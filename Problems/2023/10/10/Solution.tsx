function minOperations(nums: number[]): number {
    const n = nums.length;
    nums.sort((a, b) => a - b);

    function searchLeft(nums: number[], target: number): number {
        let l = 0, r = n;
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

    function searchRight(nums: number[], target: number): number {
        let l = 0, r = n;
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

    const dups = [];
    for (let i = 1; i < n; i++) {
        if (nums[i-1] === nums[i]) {
            dups.push(nums[i-1]);
        }
    }

    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < n; i++) {
        const l = searchLeft(nums, nums[i] - n + 1);
        const ll = searchLeft(dups, nums[i]- n + 1)
        const lr = searchRight(dups, nums[i]);
        ans = Math.min(ans, n - (i - l) - 1 + (lr - ll));
        const r = searchRight(nums, nums[i] + n - 1);
        const rl = searchLeft(dups, nums[i]);
        const rr = searchRight(dups, nums[i] + n - 1);
        ans = Math.min(ans, n - (r - i) + (rr - rl));
    }
    return ans;
};
