function lengthOfLIS(nums: number[]): number {
    let dp = Array(nums.length).fill(1), ans = 1;
    for (let i = 1; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }
    }
    return dp.reduce((a, b) => Math.max(a, b));
};
