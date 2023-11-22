function reductionOperations(nums: number[]): number {
    nums.sort((a, b) => b - a);
    let cur = nums[0], ans = 0;
    for (let i = 1; i < nums.length; i++) {
        if (cur > nums[i]) {
            cur = nums[i];
            ans += i;
        }
    }
    return ans;
};
