function search(nums: number[], target: number): number {
    let l = 0, r = nums.length;
    while (l < r) {
        const m = l + Math.floor((r - l) / 2);
        if (nums[m] === target) {
            return m;
        }
        if (nums[0] <= nums[m]) {
            if (nums[0] <= target && target < nums[m]) {
                r = m;
            } else {
                l = m + 1;
            }
        } else {
            if (nums[m] < target && target <= nums[nums.length-1]) {
                l = m + 1;
            } else {
                r = m;
            }
        }
    }
    return l < nums.length && nums[l] === target ? l : -1;
};
