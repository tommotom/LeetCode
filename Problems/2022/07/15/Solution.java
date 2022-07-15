class Solution {

  private int[][] dirs = new int[][] {{1,0}, {0,1}, {-1,0}, {0,-1}};
  private int[][] grid;
  private int rows;
  private int cols;

  public int maxAreaOfIsland(int[][] grid) {
    this.grid = grid;
    this.rows = grid.length;
    this.cols = grid[0].length;

    int ans = 0;
    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        if (grid[i][j] == 1) {
          ans = Math.max(ans, dfs(i, j));
        }
      }
    }

    return ans;
  }

  private int dfs(int i, int j) {
    grid[i][j] = 2;
    int ret = 0;
    for (int [] dir : dirs) {
      int nextI = i + dir[0];
      if (nextI < 0 || nextI >= rows) {
        continue;
      }
      int nextJ = j + dir[1];
      if (nextJ < 0 || nextJ >= cols) {
        continue;
      }
      if (grid[nextI][nextJ] == 1) {
        ret += dfs(nextI, nextJ);
      }
    }
    return ret + 1;
  }
}
