class Solution {
  public int kInversePairs(int n, int k) {
    int mod = 1000000000 + 7;
    int[][] dp = new int[n+1][k+1];
    dp[1][0] = 1;
    for (int i = 2; i < n+1; i++) {
      for (int j = 0; j < k+1; j++) {
        if (j == 0) {
          dp[i][j] = 1;
        } else {
          int val = dp[i-1][j] + mod - ((j-i)>=0 ? dp[i-1][j-i] : 0);
          val %= mod;
          dp[i][j] = (dp[i][j-1] + val) % mod;
        }
      }
    }
    return dp[n][k];
  }
}
