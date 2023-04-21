class Solution {
    public int profitableSchemes(int n, int minProfit, int[] group, int[] profit) {
        int mod = 1000000007;
        int[][] dp = new int[minProfit+1][n+1];
        dp[0][0] = 1;
        for (int i = 0; i < group.length; i++) {
            int g = group[i], p = profit[i];
            for (int j = minProfit; j >= 0; j--) {
                for (int k = n - g; k >= 0; k--) {
                    int tmp = Math.min(j + p, minProfit);
                    dp[tmp][k+g] += dp[j][k];
                    dp[tmp][k+g] %= mod;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i <= n; i++) {
            ans += dp[minProfit][i];
            ans %= mod;
        }
        return ans;
    }
}
