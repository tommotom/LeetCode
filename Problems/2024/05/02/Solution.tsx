function findMaxK(nums: number[]): number {
    nums.sort((a, b) => a - b);
    let l = 0;
    for (let r = nums.length - 1; r >= 0; r--) {
        while (l < r && Math.abs(nums[l]) > nums[r]) {
            l++;
        }
        if (-nums[l] === nums[r]) {
            return nums[r];
        }
    }
    return -1;
};
