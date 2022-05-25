class Solution {
  public int maxEnvelopes(int[][] envelopes) {
    int n = envelopes.length;
    if (n < 2) {
      return n;
    }

    Arrays.sort(envelopes, new EnvelopeComparator());
    int[] dp = new int[n];
    int size = 0;
    for (int[] envelope : envelopes) {
      int l = 0, r = size;
      while (l < r) {
        int m = l + (r - l) / 2;
        if (dp[m] < envelope[1]) {
          l = m + 1;
        } else {
          r = m;
        }
      }
      dp[l] = envelope[1];
      if (l == size) {
        size++;
      }
    }
    return size;
  }

  class EnvelopeComparator implements Comparator<int[]> {
    public int compare(int[] e1, int[] e2) {
      return e1[0] != e2[0] ? e1[0] - e2[0] : e2[1] - e1[1];
    }
  }
}
