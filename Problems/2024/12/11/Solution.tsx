function maximumBeauty(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let ans = 0, r = 0;
    for (let l = 0; l < nums.length; l++) {
        while (r + 1 < nums.length && nums[l] + 2*k >= nums[r + 1]) {
            r++;
        }
        ans = Math.max(ans, r - l + 1);
    }
    return ans;
};
