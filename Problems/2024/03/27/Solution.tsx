function numSubarrayProductLessThanK(nums: number[], k: number): number {
    if (k === 0) {
        return 0;
    }
    let ans = 0, p = 1, l = 0, r = 0;
    while (r < nums.length) {
        p *= nums[r++];
        while (l < r && p >= k) {
            p /= nums[l++];
        }
        if (p < k) {
            ans += r - l;
        }
    }
    return ans;
};
