class Solution {
  public String longestPalindrome(String s) {
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
      int l = i, r = i;
      while (l-1 >= 0 && r+1 < s.length() && s.charAt(l-1) == s.charAt(r+1)) {
        l--;
        r++;
      }
      if (end-start < r-l) {
        start = l;
        end = r;
      }

      l = i+1; r = i;
      while (l-1 >= 0 && r+1 < s.length() && s.charAt(l-1) == s.charAt(r+1)) {
        l--;
        r++;
      }
      if (end-start < r-l) {
        start = l;
        end = r;
      }
    }
    return s.substring(start, end+1);
  }
}
