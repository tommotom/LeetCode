class Solution {
  public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
    int ans = 0;
    int mod = 1000000007;
    int[][] dirs = new int[][] {{1,0}, {0,1}, {-1,0}, {0,-1}};
    int[][] dp = new int[m][n];
    dp[startRow][startColumn]++;
    for (int move = 0; move < maxMove; move++) {
      int[][] next = new int[m][n];
      for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
          for (int[] dir : dirs) {
            int nextI = i + dir[0];
            int nextJ = j + dir[1];
            if (nextI < 0 || nextI >= m || nextJ < 0 || nextJ >= n) {
              ans += dp[i][j];
              ans %= mod;
            } else {
              next[nextI][nextJ] += dp[i][j];
              next[nextI][nextJ] %= mod;
            }
          }
        }
      }
      dp = next;
    }
    return ans;
  }
}
