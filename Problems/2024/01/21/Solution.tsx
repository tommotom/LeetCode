function rob(nums: number[]): number {
    const dp = [0,0];
    for (const num of nums) {
        dp.push(Math.max(dp[dp.length-1], dp[dp.length-2] + num));
    }
    return dp[dp.length-1];
};
