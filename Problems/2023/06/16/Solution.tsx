const mod: bigint = 1000000007n;

function factorial(num: number): bigint {
    let ret: bigint = 1n;
    for (let n = 1n; n <= num; n++) {
        ret *= n;
    }
    console.log(num, ret);
    return ret;
}

function helper(nums: number[]): bigint {
    if (nums.length <= 2) {return 1n;}
    const l: number[] = nums.filter((n) => n < nums[0]);
    const r: number[] = nums.filter((n) => n > nums[0]);
    const left: bigint = helper(l);
    const right: bigint = helper(r);
    const comb: bigint = factorial(l.length + r.length) / factorial(l.length) / factorial(r.length);
    return comb * left * right;
}

function numOfWays(nums: number[]): number {
    const ret: bigint = helper(nums) - 1n;
    return ((ret % mod) as unknown) as number;
};
