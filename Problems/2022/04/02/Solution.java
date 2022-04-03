class Solution {
  public boolean validPalindrome(String s) {
    boolean deleted = false;
    int i = 0, j = s.length() - 1;
    while (i < j) {
      if (s.charAt(i) == s.charAt(j)) {
        i++;
        j--;
        continue;
      }

      if (isPalindrome(s.substring(i+1, j+1)) || isPalindrome(s.substring(i, j))) {
        return true;
      } else {
        return false;
      }
    }

    return true;
  }

  private boolean isPalindrome(String s) {
    int i = 0, j = s.length() - 1;
    while (i < j) {
      if (s.charAt(i) != s.charAt(j)) {
        return false;
      }
      i++;
      j--;
    }
    return true;
  }
}
