function combinationSum4(nums: number[], target: number): number {
    const memo = new Map();
    function helper(target: number): number {
        if (memo.has(target)) {
            return memo.get(target);
        }
        if (target === 0) {
            return 1;
        } else if (target < 0) {
            return 0;
        }
        const ret = nums.map(num => helper(target - num)).reduce((a, b) => a + b);
        memo.set(target, ret);
        return ret;
    }
    return helper(target);
};
