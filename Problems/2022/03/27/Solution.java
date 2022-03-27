class Solution {
  public int[] kWeakestRows(int[][] mat, int k) {
    PriorityQueue<int[]> q = new PriorityQueue<>((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);
    int pos = 0;
    for (int[] row : mat) {
      int l = 0, r = row.length;
      while (l < r) {
        int m = l + (r - l) / 2;
        if (row[m] == 1) {
          l = m + 1;
        } else {
          r = m;
        }
      }
      q.add(new int[]{l, pos++});
    }

    int[] ret = new int[k];
    for (int i = 0; i < k; i++) {
      ret[i] = q.remove()[1];
    }
    return ret;
  }
}
