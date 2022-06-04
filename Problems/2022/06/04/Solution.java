class Solution {

  private int n;
  private List<List<String>> ans = new ArrayList<>();


  public List<List<String>> solveNQueens(int n) {
    this.n = n;
    helper(0, new Stack<>(), new HashSet<>());
    return ans;
  }

  private void helper(int rowNum, Stack<Integer> st, Set<Integer> occupiedCols) {
    if (rowNum == n) {
      ans.add(genBoard(st));
      return;
    }
    for (int col = 0; col < n; col++) {
      if (!occupiedCols.contains(col) && validDiagonal(rowNum, col, st)) {
        occupiedCols.add(col);
        st.push(col);
        helper(rowNum+1, st, occupiedCols);
        st.pop();
        occupiedCols.remove(col);
      }
    }
  }

  private List<String> genBoard(Stack<Integer> st) {
    List<String> ret = new ArrayList<>();
    for (Integer col : st) {
      String[] row = new String[n];
      Arrays.fill(row, ".");
      row[col] = "Q";
      ret.add(String.join("", row));
    }
    Collections.reverse(ret);
    return ret;
  }

  private boolean validDiagonal(int r, int c, Stack<Integer> st) {
    int row = 0;
    for (Integer col : st) {
      int diff = r - row;
      if (c-diff == col || c+diff == col) {
        return false;
      }
      row++;
    }
    return true;
  }
}
