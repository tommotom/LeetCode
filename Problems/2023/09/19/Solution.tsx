function findDuplicate(nums: number[]): number {
    let ans = -1;
    for (let i = 0; i < nums.length; i++) {
        const j = Math.abs(nums[i]) - 1;
        if (nums[j] < 0) {
            ans = Math.abs(nums[i]);
        }
        nums[j] *= -1;
    }
    return ans;
};
