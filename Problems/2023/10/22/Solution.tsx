function maximumScore(nums: number[], k: number): number {
    let i = k, j = k, m = nums[k], ans = nums[k];
    while (i > 0 && j+1 < nums.length) {
        if (nums[i-1] > nums[j+1]) {
            m = Math.min(m, nums[--i]);
        } else {
            m = Math.min(m, nums[++j]);
        }
        ans = Math.max(ans, m * (j - i + 1));
    }
    while (i > 0) {
        m = Math.min(m, nums[--i]);
        ans = Math.max(ans, m * (j - i + 1));
    }
    while (j+1 < nums.length) {
        m = Math.min(m, nums[++j]);
        ans = Math.max(ans, m * (j - i + 1));
    }
    return ans;
};
