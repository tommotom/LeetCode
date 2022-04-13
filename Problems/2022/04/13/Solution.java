class Solution {
  public int[][] generateMatrix(int n) {
    int[][] ret = new int[n][n];
    int[][] dir = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    int i = 0, j = 0, d = 0;
    for (int k = 1; k <= n*n; k++) {
      ret[i][j] = k;

      if (k == n*n) {
        break;
      }

      int nextI = i + dir[d][0];
      int nextJ = j + dir[d][1];
      while (isInvalid(nextI, nextJ, n, ret)) {
        d = (d+1) % 4;
        nextI = i + dir[d][0];
        nextJ = j + dir[d][1];
      }

      i = nextI;
      j = nextJ;
    }

    return ret;
  }

  private boolean isInvalid(int i, int j, int n, int[][] mat) {
    if (i < 0 || i >= n) {
      return true;
    }
    if (j < 0 || j >= n) {
      return true;
    }
    return mat[i][j] != 0;
  }
}
