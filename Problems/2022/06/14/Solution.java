class Solution {
  public int minDistance(String word1, String word2) {
    int m = word1.length(), n = word2.length();
    int[][] dp = new int[m+1][n+1];
    for (int i = 0; i < m; i++) {
      dp[i+1][0] = dp[i][0] + 1;
    }
    for (int j = 0; j < n; j++) {
      dp[0][j+1] = dp[0][j] + 1;
    }
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        if (word1.charAt(i) == word2.charAt(j)) {
          dp[i+1][j+1] = dp[i][j];
        } else {
          dp[i+1][j+1] = Math.min(dp[i][j+1], dp[i+1][j]) + 1;
        }
      }
    }
    return dp[m][n];
  }
}
