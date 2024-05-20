function maximumValueSum(nums: number[], k: number, edges: number[][]): number {
    const n = nums.length;
    const dp = Array(n+1).fill(false).map(() => Array(2).fill(0));
    dp[n][1] = 0;
    dp[n][0] = Number.MIN_SAFE_INTEGER;

    for (let i = n-1; i >= 0; i--) {
        for (let isEven = 0; isEven < 2; isEven++) {
            const y = dp[i+1][isEven^1] + (nums[i] ^ k);
            const n = dp[i+1][isEven] + nums[i];
            dp[i][isEven] = Math.max(y, n);
        }
    }
    return dp[0][1];
};
