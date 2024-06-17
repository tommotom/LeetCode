function minPatches(nums: number[], n: number): number {
    let missing = 1, ans = 0, i = 0;
    while (missing <= n) {
        if (i < nums.length && nums[i] <= missing) {
            missing += nums[i++];
        } else {
            missing += missing;
            ans++;
        }
    }
    return ans;
};
