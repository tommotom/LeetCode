class Solution {
  public int maxArea(int h, int w, int[] horizontalCuts, int[] verticalCuts) {
    int n = horizontalCuts.length, m = verticalCuts.length;
    int[] hor = new int[n+2], ver = new int[m+2];
    Arrays.sort(horizontalCuts);
    Arrays.sort(verticalCuts);
    System.arraycopy(horizontalCuts, 0, hor, 1, n);
    System.arraycopy(verticalCuts, 0, ver, 1, m);
    hor[n+1] = h;
    ver[m+1] = w;

    long a = 0;
    for (int i = 1; i < n+2; i++) {
      a = Math.max(a, hor[i]-hor[i-1]);
    }
    long b = 0;
    for (int i = 1; i < m+2; i++) {
      b = Math.max(b, ver[i]-ver[i-1]);
    }
    return (int) (a*b%1000000007);
  }
}
