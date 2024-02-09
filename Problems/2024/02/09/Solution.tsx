function largestDivisibleSubset(nums: number[]): number[] {
    nums.sort((a, b) => a - b);
    const dp = [];
    for (let i = 0; i < nums.length; i++) {
        let divisor = new Set([nums[i]]);
        for (let j = 0; j < i; j++) {
            if (nums[i] % nums[j] === 0 && dp[j].size + 1 > divisor.size) {
                divisor = new Set(dp[j]);
                divisor.add(nums[i]);
            }
        }
        dp.push(divisor);
    }
    let ans: Set<number> = new Set();
    for (const d of dp) {
        if (ans.size < d.size) {
            ans = d;
        }
    }
    return Array.from(ans.values());
};
