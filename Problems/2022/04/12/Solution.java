class Solution {
  public void gameOfLife(int[][] board) {
    int m = board.length, n = board[0].length;
    int[][] ret = new int[m][n];
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        ret[i][j] = nextGen(i, j, m, n, board);
      }
    }
    for (int i = 0; i < m; i++) {
      for (int j = 0; j < n; j++) {
        board[i][j] = ret[i][j];
      }
    }
  }

  private int nextGen(int i, int j, int m, int n, int[][] board) {
    int nei = neighbors(i, j, m, n, board);
    if (board[i][j] == 1) {
      return nei == 2 || nei == 3 ? 1 : 0;
    } else {
      return nei == 3 ? 1 : 0;
    }
  }

  private int neighbors(int i, int j, int m, int n, int[][] board) {
    int ret = 0;
    if (i > 0) {
      if (j > 0) {
        ret += board[i-1][j-1];
      }
      ret += board[i-1][j];
      if (j+1 < n) {
        ret += board[i-1][j+1];
      }
    }
    if (j > 0) {
      ret += board[i][j-1];
    }
    if (j+1 < n) {
      ret += board[i][j+1];
    }
    if (i+1 < m) {
      if (j > 0) {
        ret += board[i+1][j-1];
      }
      ret += board[i+1][j];
      if (j+1 < n) {
        ret += board[i+1][j+1];
      }
    }
    return ret;
  }
}
