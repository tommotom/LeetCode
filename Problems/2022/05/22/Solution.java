class Solution {

  private int ans;

  public int countSubstrings(String s) {
    ans += s.length();
    for (int i = 0; i < s.length(); i++) {
      helper(i, i, s);
    }
    for (int i = 0; i < s.length()-1; i++) {
      helper(i+1, i, s);
    }
    return ans;
  }

  private void helper(int i, int j, String s) {
    while (i-1 >= 0 && j+1 < s.length() && s.charAt(i-1) == s.charAt(j+1)) {
      i--;
      j++;
      ans++;
    }
  }
}
