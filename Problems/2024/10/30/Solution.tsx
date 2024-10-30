function minimumMountainRemovals(nums: number[]): number {
    const n = nums.length;

    const lToR = Array(n);
    const dfs1 = (i, step) => {
        if (lToR[i] >= step) {
            return;
        }
        lToR[i] = step;
        for (let j = i+1; j < n; j++) {
            if (nums[i] < nums[j]) {
                dfs1(j, step+1);
            }
        }
    }

    for (let i = 0; i < n; i++) {
        if (lToR[i] === undefined) {
            dfs1(i, 0);
        }
    }

    const rToL = Array(nums.length);
    const dfs2 = (i, step) => {
        if (rToL[i] >= step) {
            return;
        }
        rToL[i] = step;
        for (let j = i-1; j >= 0; j--) {
            if (nums[j] > nums[i]) {
                dfs2(j, step+1);
            }
        }
    }
    for (let i = n-1; i >= 0; i--) {
        if (rToL[i] === undefined) {
            dfs2(i, 0);
        }
    }

    let ans = n;
    for (let i = 1; i < n-1; i++) {
        if (lToR[i] > 0 && rToL[i] > 0) {
            ans = Math.min(ans, n - lToR[i] - rToL[i] - 1);
        }
    }

    return ans;
};
