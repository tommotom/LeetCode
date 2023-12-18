function maxProductDifference(nums: number[]): number {
    nums.sort((a, b) => a - b);
    return nums[nums.length-1] * nums[nums.length-2] - nums[1] * nums[0];
};
