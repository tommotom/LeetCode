function findDuplicates(nums: number[]): number[] {
    const hasOne: {
        [num: number]: true
    } = {};
    const result: number[] = [];

    for (let i = 0; i < nums.length; i++) {
        if (!hasOne[nums[i]]) {
            hasOne[nums[i]] = true;
        } else {
            result.push(nums[i]);
        }
    }
    return result;
};
