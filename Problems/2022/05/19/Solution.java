class Solution {

  private int ans;
  private int rows;
  private int cols;
  private int[][] matrix;
  private int[][] path;

  public int longestIncreasingPath(int[][] matrix) {
    this.rows = matrix.length;
    this.cols = matrix[0].length;
    this.matrix = matrix;
    this.path = new int[rows][cols];

    for (int row = 0; row < rows; row++) {
      for (int col = 0; col < cols; col++) {
        if (isPeak(row, col)) {
          dfs(row, col);
        }
      }
    }
    return ans + 1;
  }

  private boolean isPeak(int r, int c) {
    if (r > 0 && matrix[r-1][c] > matrix[r][c]) {
      return false;
    }
    if (c > 0 && matrix[r][c-1] > matrix[r][c]) {
      return false;
    }
    if (r+1 < rows && matrix[r+1][c] > matrix[r][c]) {
      return false;
    }
    if (c+1 < cols && matrix[r][c+1] > matrix[r][c]) {
      return false;
    }
    return true;
  }

  private void dfs(int r, int c) {
    ans = Math.max(ans, path[r][c]);
    if (r > 0 && matrix[r-1][c] < matrix[r][c] && path[r-1][c] <= path[r][c]) {
      path[r-1][c] = path[r][c] + 1;
      dfs(r-1, c);
    }
    if (c > 0 && matrix[r][c-1] < matrix[r][c] && path[r][c-1] <= path[r][c]) {
      path[r][c-1] = path[r][c] + 1;
      dfs(r, c-1);
    }
    if (r+1 < rows && matrix[r+1][c] < matrix[r][c] && path[r+1][c] <= path[r][c]) {
      path[r+1][c] = path[r][c] + 1;
      dfs(r+1, c);
    }
    if (c+1 < cols && matrix[r][c+1] < matrix[r][c] && path[r][c+1] <= path[r][c]) {
      path[r][c+1] = path[r][c] + 1;
      dfs(r, c+1);
    }
  }
}
