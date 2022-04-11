class Solution {
  public int calPoints(String[] ops) {
    int[] scores = new int[ops.length];
    int i = 0;
    for (String s: ops) {
      if (s.equals("+")) {
        scores[i] = scores[i-1] + scores[i-2];
        i++;
      } else if (s.equals("C")) {
        i--;
        scores[i] = 0;
      } else if (s.equals("D")) {
        scores[i] = scores[i-1] * 2;
        i++;
      } else {
        scores[i] = Integer.parseInt(s);
        i++;
      }
    }
    return Arrays.stream(scores).sum();
  }
}
