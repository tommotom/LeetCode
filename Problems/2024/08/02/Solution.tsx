function minSwaps(nums: number[]): number {
    const memo = []
    let zeros = 0, ones = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) {
            zeros++;
        } else {
            ones++;
        }
        memo.push(zeros);
    }

    if (zeros <= 1) {
        return 0;
    }

    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < nums.length; i++) {
        if (i + ones < nums.length) {
            ans = Math.min(ans, memo[i + ones] - memo[i]);
        } else {
            const surplus = i + ones - nums.length;
            ans = Math.min(ans, memo[nums.length-1] - memo[i] + memo[surplus]);
        }
    }

    return ans;
};
