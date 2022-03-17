class Solution {
  public int scoreOfParentheses(String s) {
    if (s.isEmpty()) {
      return 0;
    }
    int score = 0;
    int level = 0;
    int i = 0;
    int start = 0;
    while (i < s.length()) {
      if (s.charAt(i) == '(') {
        level++;
      } else if (s.charAt(i) == ')') {
        level--;
      }

      if (level == 0) {
        if (start + 1 == i) {
          score++;
        } else {
          score += scoreOfParentheses(s.substring(start+1, i)) * 2;
        }
        start = i+1;
      }

      i++;
    }

    return score;
  }
}
