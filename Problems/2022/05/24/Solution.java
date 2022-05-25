class Solution {
  public int longestValidParentheses(String s) {
    int ans = 0;

    int l = 0, r = 0;
    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if (c == '(') {
        l++;
      } else {
        r++;
      }
      if (l == r) {
        ans = Math.max(ans, l+r);
      } else if (l < r) {
        l = 0;
        r = 0;
      }
    }

    l = 0; r = 0;
    for (int i = s.length()-1; i >= 0; i--) {
      char c = s.charAt(i);
      if (c == ')') {
        r++;
      } else {
        l++;
      }
      if (l == r) {
        ans = Math.max(ans, l+r);
      } else if (l > r) {
        l = 0;
        r = 0;
      }
    }

    return ans;
  }
}
