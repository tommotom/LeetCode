function minIncrementForUnique(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let ans = 0;
    for (let i = 0; i < nums.length - 1; i++) {
        if (nums[i+1] <= nums[i]) {
            ans += nums[i] - nums[i+1] + 1;
            nums[i+1] = nums[i] + 1;
        }
    }
    return ans;
};
