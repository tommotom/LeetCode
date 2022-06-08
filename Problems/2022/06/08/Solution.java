class Solution {
  public int removePalindromeSub(String s) {
    if (isPalindrome(s)) {
      return 1;
    }
    return 2;
  }

  private boolean isPalindrome(String s) {
    for (int i = 0, j = s.length()-1; i < j; i++, j--) {
      if (s.charAt(i) != s.charAt(j)) {
        return false;
      }
    }
    return true;
  }
}
