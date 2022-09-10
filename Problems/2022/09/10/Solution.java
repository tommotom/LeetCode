class Solution {
    public int maxProfit(int k, int[] prices) {
        int n = prices.length;
        if (n == 0 || k == 0) {return 0;}
        int[][] dp = new int[k+1][n];
        for (int i = 1; i < k+1; i++) {
            int prev = -prices[0];
            for (int j = 1; j < n; j++) {
                dp[i][j] = Math.max(dp[i][j-1], prev + prices[j]);
                prev = Math.max(prev, dp[i-1][j] - prices[j]);
            }
        }
        return dp[k][n-1];
    }
}
