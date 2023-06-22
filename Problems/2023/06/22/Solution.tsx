function maxProfit(prices: number[], fee: number): number {
    const dp = new Array(prices.length);
    dp[0] = 0;
    let val = prices[0] + fee;
    for (let i = 1; i < prices.length; i++) {
        dp[i] = Math.max(dp[i-1], prices[i] - val);
        val = Math.min(val, prices[i] + fee - dp[i-1]);
    }
    return dp.reduce((a, b) => Math.max(a, b));
};
