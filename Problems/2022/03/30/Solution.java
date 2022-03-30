class Solution {
  public boolean searchMatrix(int[][] matrix, int target) {
    int rows = matrix.length, cols = matrix[0].length;

    int u = 0, d = rows;
    while (u < d) {
      int row = u + (d - u) / 2;
      if (matrix[row][cols-1] < target) {
        u = row + 1;
      } else {
        d = row;
      }
    }

    if (u == rows) {
      return false;
    }

    int l = 0, r = cols;
    while(l < r) {
      int col = l + (r - l) / 2;
      if (matrix[u][col] < target) {
        l = col + 1;
      } else {
        r = col;
      }
    }

    if (l == cols) {
      return false;
    }

    return matrix[u][l] == target;
  }
}
