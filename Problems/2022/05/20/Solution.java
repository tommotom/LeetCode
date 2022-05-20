class Solution {
  public int uniquePathsWithObstacles(int[][] obstacleGrid) {
    int rows = obstacleGrid.length, cols = obstacleGrid[0].length;
    if (obstacleGrid[0][0] == 1 || obstacleGrid[rows-1][cols-1] == 1) {
      return 0;
    }

    int[][] dp = new int[rows][cols];
    dp[0][0] = 1;
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (obstacleGrid[i][j] == 1) {
          continue;
        }
        if (i > 0 && obstacleGrid[i-1][j] == 0) {
          dp[i][j] += dp[i-1][j];
        }
        if (j > 0 && obstacleGrid[i][j-1] == 0) {
          dp[i][j] += dp[i][j-1];
        }
      }
    }
    return dp[rows-1][cols-1];
  }
}
