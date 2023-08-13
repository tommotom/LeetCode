function validPartition(nums: number[]): boolean {
    const memo: Map<number, boolean> = new Map();
    function helper(i: number): boolean {
        if (i === nums.length) {
            return true;
        }
        if (memo.has(i)) {
            return memo.get(i);
        }
        let ret: boolean = false;
        if (i+1 < nums.length && nums[i] === nums[i+1]) {
            ret ||= helper(i+2);
        }
        if (i+2 < nums.length && nums[i] === nums[i+1] && nums[i+1] === nums[i+2]) {
            ret ||= helper(i+3);
        }
        if (i+2 < nums.length && nums[i]+1 === nums[i+1] && nums[i+1]+1 === nums[i+2]) {
            ret ||= helper(i+3);
        }
        memo.set(i, ret);
        return ret;
    }
    return helper(0);
};
