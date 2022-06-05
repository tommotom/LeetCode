class Solution {

  private int ans;
  private int n;

  public int totalNQueens(int n) {
    this.n = n;
    helper(0, 0, 0, 0);
    return ans;
  }

  private void helper(int row, int colMask, int diMask1, int diMask2) {
    if (row == n) {
      ans++;
      return;
    }
    for (int col = 0; col < n; col++) {
      if (isValid(row, col, colMask, diMask1, diMask2)) {
        colMask |= 1<<col;
        diMask1 |= 1<<(row+col);
        diMask2 |= 1<<(n-row+col-1);
        helper(row+1, colMask, diMask1, diMask2);
        colMask ^= 1<<col;
        diMask1 ^= 1<<(row+col);
        diMask2 ^= 1<<(n-row+col-1);
      }
    }
  }

  private boolean isValid(int row, int col, int colMask, int diMask1, int diMask2) {
    if (((1<<col) & colMask) != 0) {
      return false;
    }
    if ((1<<(row+col) & diMask1) != 0) {
      return false;
    }
    if ((1<<(n-row+col-1) & diMask2) != 0) {
      return false;
    }
    return true;
  }
}
