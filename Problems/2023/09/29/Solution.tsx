function isMonotonic(nums: number[]): boolean {
    let isIncreasing: boolean;
    for (let i = 0; i < nums.length-1; i++) {
        if (nums[i] < nums[i+1]) {
            if (isIncreasing !== undefined && !isIncreasing) {
                return false;
            }
            isIncreasing = true;
        } else if (nums[i] > nums[i+1]) {
            if (isIncreasing !== undefined && isIncreasing) {
                return false;
            }
            isIncreasing = false;
        }
    }
    return true;
};
