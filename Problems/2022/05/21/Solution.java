class Solution {
  public int coinChange(int[] coins, int amount) {
    int[] dp = new int[amount+1];
    Arrays.fill(dp, -1);
    dp[0] = 0;
    for (int i = 0; i < dp.length; i++) {
      for (int coin : coins) {
        if (i - coin >= 0 && dp[i-coin] != -1) {
          dp[i] = dp[i] == -1 ? dp[i-coin] + 1 : Math.min(dp[i], dp[i-coin] + 1);
        }
      }
    }
    return dp[amount];
  }
}
