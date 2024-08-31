function twoSum(nums: number[], target: number): number[] {
    const seen = new Map();
    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        if (seen.has(target - num)) {
            return [seen.get(target - num), i];
        }
        seen.set(num, i);
    }
    return [];
};
