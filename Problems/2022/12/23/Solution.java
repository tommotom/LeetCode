class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int min = prices[0];
        int diff = -prices[0];
        int[] dp = new int[n];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(dp[i-1], prices[i]-min);
            dp[i] = Math.max(dp[i], diff+prices[i]);
            min = Math.min(min, prices[i]);
            if (i > 1) {
                diff = Math.max(diff, dp[i-2] - prices[i]);
            }
        }
        return dp[n-1];
    }
}
