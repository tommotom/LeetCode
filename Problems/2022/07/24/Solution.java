class Solution {
  public boolean searchMatrix(int[][] matrix, int target) {
    int m = matrix.length, n = matrix[0].length;

    int u = 0, d = m;
    while (u < d) {
      int r = u + (d - u) / 2;
      if (matrix[r][n-1] < target) {
        u = r + 1;
      } else {
        d = r;
      }
    }

    for (int row = u; row < m; row++) {
      if (matrix[row][0] > target) {
        break;
      }
      int l = 0, r = n-1;
      while (l < r) {
        int c = l + (r - l) / 2;
        if (matrix[row][c] == target) {
          return true;
        } else if (matrix[row][c] < target) {
          l = c + 1;
        } else {
          r = c;
        }
      }
      if (l < n && matrix[row][l] == target) {
        return true;
      }
    }
    return false;
  }
}
