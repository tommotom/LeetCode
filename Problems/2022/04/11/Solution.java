class Solution {
  public List<List<Integer>> shiftGrid(int[][] grid, int k) {
    if (grid == null || grid[0] == null) {
      return null;
    }
    int m = grid.length, n = grid[0].length;
    k %= m * n;
    List<List<Integer>> ans = new ArrayList<>();
    for (int i = 0; i < m; i++) {
      List<Integer> row = new ArrayList<>();
      for (int j = 0; j < n; j++) {
        int r = (m * n + i + (m * n + j - k) / n) % m;
        int c = (m * n + j - k) % n;
        row.add(grid[r][c]);
      }
      ans.add(row);
    }
    return ans;
  }
}
