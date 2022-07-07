class Solution {

  Set<Integer> visited = new HashSet<>();
  String s1;
  String s2;
  String s3;

  public boolean isInterleave(String s1, String s2, String s3) {
    if (s1.length() + s2.length() != s3.length()) {
      return false;
    }
    this.s1 = s1;
    this.s2 = s2;
    this.s3 = s3;

    return helper(0, 0, 0);
  }

  private boolean helper(int i, int j, int k) {
    if (k == s3.length()) {
      return true;
    }
    if (visited.contains(hash(i, j, k))) {
      return false;
    }
    if (i < s1.length() && s1.charAt(i) == s3.charAt(k) && helper(i+1, j, k+1)) {
      return true;
    }
    if (j < s2.length() && s2.charAt(j) == s3.charAt(k) && helper(i, j+1, k+1)) {
      return true;
    }
    visited.add(hash(i, j, k));
    return false;
  }

  private int hash(int i, int j, int k) {
    return i*10000 + j*100 + k;
  }
}
