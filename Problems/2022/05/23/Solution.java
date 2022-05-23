class Solution {
  public int findMaxForm(String[] strs, int m, int n) {
    int[][] dp = new int[m+1][n+1];

    int ans = 0;
    for (String str : strs) {
      int zeros = 0, ones = 0;
      for (char c : str.toCharArray()) {
        if (c == '0') zeros++;
        else ones++;
      }
      for (int i = m; i >= zeros; i--) {
        for (int j = n; j >= ones; j--) {
          dp[i][j] = Math.max(dp[i-zeros][j-ones] + 1, dp[i][j]);
        }
      }
    }
    return dp[m][n];
  }
}
