class Solution {
  public int minDominoRotations(int[] tops, int[] bottoms) {
    int n = tops.length;
    int ans = n+1;

    for (int num = 1; num < 7; num++) {
      boolean isValid = true;
      int top = 0, bottom = 0;
      for (int i = 0; i < n; i++) {
        if (tops[i] != num && bottoms[i] != num) {
          isValid = false;
          break;
        }
        if (tops[i] != num) {
          top++;
        }
        if (bottoms[i] != num) {
          bottom++;
        }
      }
      if (isValid) {
        ans = Math.min(ans, Math.min(top, bottom));
      }
    }

    return ans == n+1 ? -1 : ans;
  }
}
