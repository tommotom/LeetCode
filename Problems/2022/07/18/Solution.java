class Solution {
  public int numSubmatrixSumTarget(int[][] matrix, int target) {
    int row = matrix.length;
    int col = matrix[0].length;

    int[][] cum = new int[row][col];
    for (int i = 0; i < row; i++) {
      for (int j = 0; j < col; j++) {
        if (i > 0) {
          cum[i][j] += cum[i-1][j];
        }
        cum[i][j] += matrix[i][j];
      }
    }

    int ans = 0;
    for (int r1 = -1; r1 < row-1; r1++) {
      for (int r2 = r1+1; r2 < row; r2++) {
        HashMap<Integer, Integer> count = new HashMap<>();
        count.put(0, 1);
        int sum = 0;
        for (int c = 0; c < col; c++) {
          sum += cum[r2][c] - (r1 >= 0 ? cum[r1][c] : 0);
          if (count.containsKey(sum - target)) {
            ans += count.get(sum - target);
          }
          count.put(sum, count.getOrDefault(sum, 0)+1);
        }
      }
    }
    return ans;
  }
}