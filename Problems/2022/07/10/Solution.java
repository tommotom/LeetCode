class Solution {
  public int minCostClimbingStairs(int[] cost) {
    int[] dp = new int[cost.length+1];
    Arrays.fill(dp, 1000000);
    dp[0] = 0; dp[1] = 0;
    for (int i = 0; i < cost.length; i++) {
      int tmp = dp[i] + cost[i];
      dp[i+1] = Math.min(dp[i+1], tmp);
      if (i < cost.length-1) {
        dp[i+2] = Math.min(dp[i+2], tmp);
      }
    }
    return dp[cost.length];
  }
}
